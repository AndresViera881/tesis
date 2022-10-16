import smtplib
import uuid
from datetime import datetime, date
from email.message import EmailMessage

from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity

from flask_jwt_extended import create_access_token, current_user, jwt_required as jwt_required_extend, get_jwt_identity

from flask_bcrypt import Bcrypt
from itsdangerous import URLSafeTimedSerializer, SignatureExpired

import db
from models.clientela import UsuarioModel, TblCitas

bc = Bcrypt()
s = URLSafeTimedSerializer('__SECRET_KEY__')


class ClientelaList(Resource):
    @jwt_required()
    def get(self):
        users = UsuarioModel.query.all()
        return {'users': list(map(lambda x: x.json(), users))}, 200


class LoginClient(Resource):
    parse = reqparse.RequestParser()
    parse.add_argument('email', type=str, required=True, help='This field cannot be blank')
    parse.add_argument('password', type=str, required=True, help='This field cannot be blank')

    @jwt_required_extend
    def get(self):
        current_user = get_jwt_identity()
        user = UsuarioModel.find_by_id(current_user)
        if user:
            return user.json()
        return {'message': "User not found"}

    def post(self):
        data = LoginClient.parse.parse_args()
        user = UsuarioModel.find_by_correo(data["email"])
        if user and bc.check_password_hash(user.password, data['password']):
            access_token = create_access_token(identity=user.id)
            id = user.id
            print(access_token)
            return jsonify(access_token=access_token, id=id)
        #       return {"access_token": access_token}
        else:
            return {"Wrong username or password"}, 401


class ClienteResours(Resource):
    parse = reqparse.RequestParser()
    parse.add_argument('nombre', type=str, required=True, help='This field cannot be blank')
    parse.add_argument('apellidos', type=str, required=True, help='This field cannot be blank')
    parse.add_argument('cedula', type=str, required=True, help='This field cannot be blank')
    parse.add_argument('sexo', type=str, required=True, help='This field cannot be blank')
    parse.add_argument('direccion', type=str, required=True, help='This field cannot be blank')
    parse.add_argument('fecha_nacimiento', type=datetime, help='This field cannot be blank', default=date.today())
    parse.add_argument('correo', type=str, required=True, help='This field cannot be blank')
    parse.add_argument('password', type=str, required=True, help='This field cannot be blank')
    parse.add_argument('telefono', type=str, required=True, help='This field cannot be blank')

    def post(self):
        data = ClienteResours.parse.parse_args()
        try:
            if UsuarioModel.find_by_correo(data["correo"]):
                return {"message": "An usuario with name '{}' already exists".format(data['correo'])}, 400

            cliente = UsuarioModel(str(uuid.uuid4()), data['nombre'], data['apellidos'], data['cedula'],
                                   data['sexo'], data['direccion'], data['fecha_nacimiento'], data['correo'],
                                   bc.generate_password_hash(data['password']).decode('utf-8'), data['telefono'])

            cliente.save_to_db()
            token = s.dumps(data["correo"], 'opticapruebas2021@gmail.com')
            msg = EmailMessage()
            msg['Subject'] = 'Registro de citas'
            msg['From'] = 'Andres'
            msg['To'] = data["correo"]
            msg.set_content(
                'Se ha registrado exitosamente, para acceder a la cita proceda a la confirmacion de su registro' + ' ' +
                'http://localhost:5000/auth/confirmar_email/' + token + '/' + data["correo"])
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            #OpticaPruebas.2021
            server.login('opticapruebas2021@gmail.com', 'pwugdritdygedrur')
            server.send_message(msg)
            server.quit()
        except:
            return {"message": "An error occured inserting the clientela."}, 500
        return cliente.json(), 201

    @jwt_required_extend
    def put(self):
        id = get_jwt_identity()
        data = ClienteResours.parse.parse_args()
        cliente = UsuarioModel.find_by_id(id)
        if cliente:
            cliente.nombres = data['nombre']
            cliente.apelidos = data['apellidos']
            cliente.cedula = data['cedula']
            cliente.sexo = data['sexo']
            cliente.direccion = data['direccion']
            cliente.fecha_nacimiento = data['fecha_nacimiento']
            cliente.correo = data['correo']
            cliente.password = bc.generate_password_hash(data['password']).decode('utf-8')
            cliente.telefono = data['telefono']
        else:
            cliente = UsuarioModel(id, **data)
        try:
            cliente.save_to_db()
        except:
            return {"error": True, "message": "User data is not Updated !!! Try again"}, 500

        return {"error": False, "message": "User Data is Updated"}, 200

    @jwt_required()
    def delete(self, id):
        if current_identity.super_admin == True or current_identity.admin_clientela == True:
            cliente = UsuarioModel.find_by_id(id)
            if cliente:
                cliente.delete_from_db()
                return {"message": "client delete"}, 200
            return {"message": "client not found"}
        return {"message": "You dont have authorization"}, 401


class confirma_email(Resource):
    def get(self, token, correo):
        try:
            email = s.loads(
                token, salt='opticapruebas2021@gmail.com', max_age=3600)
            confirmar = UsuarioModel.query.filter_by(correo=correo).first()
            if not confirmar:
                return {"respuesta": 'Verificacion no encontrada'}, 404
            confirmar.verificacion_email = True
            confirmar.save_to_db()

        except SignatureExpired:
            return jsonify(respuesta='El token ha expirado')
        return {"message": email}
        # return jsonify(respuesta="Token correcto!")

    def post(self, token, correo):
        try:
            email = s.loads(token, salt='opticapruebas2021@gmail.com', max_age=3600)
            confirmar = UsuarioModel.query.get(correo)
            if not confirmar:
                return {"respuesta": 'Verificacion no encontrada'}, 404
            confirmar.verificacion_email = True
            confirmar.save_to_db()
            # return {"message": email}

        except SignatureExpired:
            return jsonify(respuesta='El token ha expirado')
        return {"message": email}
        # return jsonify(respuesta="Token correcto!")


class CitasResour(Resource):
    parse = reqparse.RequestParser()
    parse.add_argument('fecha', required=True, help='This field cannot be blank')
    parse.add_argument('hora', required=True, help='This field cannot be blank')
    parse.add_argument('estado', type=bool, required=True, help='This field cannot be blank')
    parse.add_argument('cliente_id', type=int, required=True, help='This field cannot be blank')
    parse.add_argument('medico_id', type=int, required=True, help='This field cannot be blank')
    parse.add_argument('horario_id', type=int, required=True, help='This field cannot be blank')

    @jwt_required()
    def post(self):
        data = CitasResour.parse.parse_args()
        if current_user.super_admin == True or current_user.admin_clientela == True:
            cita = TblCitas(data['fecha'], data['hora'], data['estado'],
                            data['cliente_id'], data['medico_id'], data['horario_id'])
            try:
                cita.save_to_db()
            except:
                return {"message": "An error occured inserting the cita."}, 500
            return cita.json(), 201
        else:
            return {"message": "You don't have authorisation"}, 401

    @jwt_required()
    def delete(self, cliente_id):
        cital = TblCitas.find_by_cliente_id(cliente_id)
        if cital:
            cital.delete_from_db()
            return {'message': "user deleted"}, 200
        return {"message": "cita not found"}


class CitaList(Resource):
    @jwt_required()
    def get(self):
        citas = TblCitas.query.all()
        if citas:
            return {"citas_list": list(map(lambda x: x.json(), citas))}, 200


class CitaListById(Resource):
    @jwt_required()
    def get(self, id):
        citas = TblCitas.find_by_id(id)
        if citas:
            return citas.json()
        return {"message": "Paciente no encontrado"}, 404

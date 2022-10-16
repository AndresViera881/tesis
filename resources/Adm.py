from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity
from flask_bcrypt import Bcrypt

from models.adm import AdminUsuario
from models.clientela import UsuarioModel

bc = Bcrypt()


class AdmResoure(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("cedula", type=str, help='Este campo no puede estar vacio', required=True)
    parser.add_argument("nombres", type=str, help='Este campo no puede estar vacio', required=True)
    parser.add_argument("apellidos", type=str, help='Este campo no puede estar vacio', required=True)
    parser.add_argument("correo", type=str, help='Este campo no puede estar vacio', required=True)
    parser.add_argument("password", type=str, help='Este campo no puede estar vacio', required=True)
    parser.add_argument("direccion", type=str, help='Este campo no puede estar vacio', required=True)
    parser.add_argument("telefono", type=str, help='Este campo no puede estar vacio', required=True)
    parser.add_argument("sexe", type=str, help='Este campo no puede estar vacio', required=True)
    parser.add_argument("admin_clientela", type=bool, help='Este campo no puede estar vacio', required=False)
    parser.add_argument("admin_hospital", type=bool, help='Este campo no puede estar vacio', required=True)
    parser.add_argument("super_admin", type=bool, help='Este campo no puede estar vacio', required=False)

    #
    # @jwt_required()
    # def getById(self, id):
    #     if current_identity.super_admin == True:
    #         usuario = AdminUsuario.find_by_id(id)
    #         return {"usuarios": list(map(lambda x: x.json(), usuario))}, 200
    #     else:
    #         return {"message": "Authorization..."}, 401

    @jwt_required()
    def post(self):
        data = AdmResoure.parser.parse_args()
        if not current_identity.super_admin:
            return {"message": "No tiene autorizacion"}, 401

        if AdminUsuario.find_by_correo(data["correo"]):
            return {"message": "El usuario con el correo '{}' ya existe".format(data['correo'])}, 400

        if AdminUsuario.find_by_cedula(data["cedula"]):
            return {"message": "El usuario con la cedula '{}' ya existe".format(data['cedula'])}, 400

        usuarios = AdminUsuario(data['cedula'], data['nombres'], data['apellidos'], data['correo'],
                                bc.generate_password_hash(data['password']).decode('utf-8'), data['direccion']
                                , data['telefono'], data['sexe'], data['admin_clientela'], data['admin_hospital'],
                                data['super_admin'])

        try:
            usuarios.save_to_db()
        except:
            return {"message": "Error al insertar el usuario"}, 500

        return usuarios.json(), 201

    @jwt_required()
    def put(self, id):
        data = AdmResoure.parser.parse_args()
        if not current_identity.super_admin:
            return {"message": "You do not have authorization"}, 401

        user = AdminUsuario.find_by_id(id)

        if user:
            user.cedula = data['cedula']
            user.nombre = data['nombre']
            user.apellidos = data['apellidos']
            user.correo = data['correo']
            user.password = bc.generate_password_hash(data['password']).decode('utf-8')
            user.direccion = data['direccion']
            user.telefono = data['telefono']
            user.sexe = data['sexe']
            user.admin_clientela = data['admin_clientela']
            user.admin_hospital = data['admin_hospital']
            user.super_admin = data['super_admin']

        else:
            user = AdminUsuario(id, **data)

        try:
            user.save_to_db()
        except:
            return {"error": True, "message": "User data is not Updated !!! Try again"}

        return {"error": False, "message": "User Data is Updated"}, 200

    @jwt_required()
    def delete(self, id):
        if not current_identity.super_admin:
            return {"message": "No tiene autorizacion"}, 401
        user = AdminUsuario.find_by_id(id)
        if user:
            user.delete_from_db()
            return {'message': "usuario elimiando"}, 200
        return {"message": 'usuario no encontrado'}, 404


class AdmUsuarioUpdat(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("cedula", type=str, help='Este campo no puede estar vacio', required=True)
    parser.add_argument("nombres", type=str, help='Este campo no puede estar vacio', required=True)
    parser.add_argument("apellidos", type=str, help='Este campo no puede estar vacio', required=True)
    parser.add_argument("correo", type=str, help='Este campo no puede estar vacio', required=True)
    parser.add_argument("password", type=str, help='Este campo no puede estar vacio', required=True)
    parser.add_argument("direccion", type=str, help='Este campo no puede estar vacio', required=True)
    parser.add_argument("telefono", type=str, help='Este campo no puede estar vacio', required=True)
    parser.add_argument("sexe", type=str, help='Este campo no puede estar vacio', required=True)
    parser.add_argument("admin_clientela", type=bool)
    parser.add_argument("admin_hospital", type=bool)
    parser.add_argument("super_admin", type=bool)

    @jwt_required()
    def put(self, id):
        data = AdmUsuarioUpdat.parser.parse_args()
        if current_identity.super_admin == True or current_identity.admin_clientela == True or current_identity.admin_hospital == True:
            user = AdminUsuario.find_by_id(id)
            data = AdmUsuarioUpdat.parser.parse_args()

            if user:
                user.cedula = data['cedula']
                user.nombres = data['nombres']
                user.apellidos = data['apellidos']
                user.correo = data['correo']
                user.password = bc.generate_password_hash(data['password']).decode('utf-8')
                user.direccion = data['direccion']
                user.telefono = data['telefono']
                user.sexe = data['sexe']
                user.admin_clientela = data['admin_clientela']
                user.admin_hospital = data['admin_hospital']
                user.super_admin = data['super_admin']
            else:
                user = AdminUsuario(id, **data)

            try:
                user.save_to_db()
            except:
                return {"error": True, "message": "User data is not Updated !!! Try again"}

            return user.json()  # {"error": False, "message": "User Data is Updated"}, 200
        else:
            return {"message": "You do not have authorization"}, 401


class AdmResoureList(Resource):
    @jwt_required()
    def get(self):
        if current_identity.super_admin == True:
            usuarios = AdminUsuario.query.all()
            return {"usuarios": list(map(lambda x: x.json(), usuarios))}, 200

        return {"message": "Authorization..."}, 401


class AdmResoureListById(Resource):
    def get(self, id):
        admUsuario = AdminUsuario.find_by_id(id)
        if admUsuario:
            return admUsuario.json()
        return {"message": "Usuario no encontrado"}, 404


class ClientelaList(Resource):
    @jwt_required()
    def get(self):
        if current_identity.super_admin == True or current_identity.admin_clientela == True:
            clientela = UsuarioModel.query.all()
            return {"clients": list(map(lambda x: x.json(), clientela))}, 200
        else:
            return {"message": "You do not have authorization"}, 400

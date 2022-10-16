from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity
from flask_bcrypt import Bcrypt
from models.paciente import PacienteModel

bc = Bcrypt()


class PacientResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("codigo", type=str, help="Este campo es requerido", required=True)
    parser.add_argument("cedula", type=str, help="Este campo es requerido", required=True)
    parser.add_argument("nombres", type=str, help="Este campo es requerido", required=True)
    parser.add_argument("apellidos", type=str, help="Este campo es requerido", required=True)
    parser.add_argument("fecha_nacimiento", type=str, help="Este campo es requerido", required=False)
    parser.add_argument("correo", type=str, help="Este campo es requerido", required=True)
    parser.add_argument("direccion", type=str, help="Este campo es requerido", required=True)
    parser.add_argument("ocupacion", type=str, help="Este campo es requerido", required=True)
    parser.add_argument("telefono", type=str, help="Este campo es requerido", required=True)
    parser.add_argument("estado", type=bool, help="Este campo es requerido", required=False)
    parser.add_argument("sucursal_id", type=int, help="Este campo es requerido", required=True)
    parser.add_argument("observacion", type=str, required=False)
    parser.add_argument("observacionAvance", type=str, required=False)
    parser.add_argument("fecha_creacion", type=str, required=False)

    @jwt_required()
    def get(self, id):
        if current_identity.super_admin == True or current_identity.admin_hospital == True:

            paciente = PacienteModel.find_by_id(id)
            if paciente:
                return paciente.json()
            return {"message": "Paciente no encontrado"}, 404
        else:
            return {"message": "No eres administrador"}, 401

    @jwt_required()
    def post(self):
        data = PacientResource.parser.parse_args()
        if current_identity.super_admin == True or current_identity.admin_hospital == True:

            if PacienteModel.find_by_cedula(data["cedula"]):
                return {"message": "An cedula with name '{}' already exists".format(data['cedula'])}, 400

            if PacienteModel.find_by_codigo(data["codigo"]):
                return {"message": "An codigo with name '{}' already exists".format(data['codigo'])}, 400

            if PacienteModel.find_by_correo(data["correo"]):
                return {"message": "An correo with name '{}' already exists".format(data['correo'])}, 400

            paciente = PacienteModel(data['codigo'], data['cedula'], data['nombres'], data['apellidos'],
                                     data['fecha_nacimiento'], data['correo'], data['direccion'], data['ocupacion'],
                                     data['telefono'], data['estado'], data['sucursal_id'],
                                     data['observacion'], data['observacionAvance'],
                                     data['fecha_creacion'])
            # try:
            paciente.save_to_db()
            # except:
            #     return {"message": "An error occured inserting the examen."}, 500
            #
            return paciente.json(), 201
        else:
            return {"message": "You don't have authorisation"}, 401

    @jwt_required()
    def put(self, id):
        if current_identity.super_admin == True or current_identity.admin_hospital == True:
            paciente = PacienteModel.find_by_id(id)
            data = PacientResource.parser.parse_args()

            if paciente:
                paciente.codigo = data['codigo']
                paciente.cedula = data['cedula']
                paciente.nombres = data['nombres']
                paciente.apellidos = data['apellidos']
                paciente.fecha_nacimiento = data['fecha_nacimiento']
                paciente.correo = data['correo']
                paciente.direccion = data['direccion']
                paciente.ocupacion = data['ocupacion']
                paciente.telefono = data['telefono']
                paciente.estado = data['estado']
                paciente.sucursal_id = data['sucursal_id']
                paciente.observacion = data['observacion']
                paciente.observacionAvance = data['observacionAvance']
                paciente.fecha_creacion = data['fecha_creacion']

            else:
                paciente = PacienteModel(id, **data)

            try:
                paciente.save_to_db()
            except:
                return {"message": "An error occured update the Paciente"}

            return paciente.json()
        else:
            return {"message": "You don't have authorisation"}, 401

    @jwt_required()
    def delete(self, id):
        if current_identity.super_admin == True or current_identity.admin_hospital == True:
            paciente = PacienteModel.find_by_id(id)
            if paciente:
                paciente.delete_from_db()
                return {'message': "Paciente deleted"}

            return {"message": 'Paciente not found'}, 404
        else:
            return {"message": "You are not admin"}, 401


class PacienteLists(Resource):
    @jwt_required()
    def get(self):
        if current_identity.super_admin == True or current_identity.admin_hospital == True:
            paciente = PacienteModel.query.all()
            return {'pacientes': list(map(lambda x: x.json(), paciente))}, 200
        else:
            return {"message": "You are not admin"}, 401

from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity
from flask_bcrypt import Bcrypt

from models.adm import AdminUsuario
from models.medico import MedicoModel, MedicoSpecialidadModel, HorarioModel

bc = Bcrypt()


class MedicoResoure(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("codigo", type=str, help='Este campo no puede estar vacio', required=True)
    parser.add_argument("cedula", type=str, help='Este campo no puede estar vacio', required=True)
    parser.add_argument("nombre", type=str, help='Este campo no puede estar vacio', required=True)
    parser.add_argument("apellidos", type=str, help='Este campo no puede estar vacio', required=True)
    parser.add_argument("telefono", type=str, help='Este campo no puede estar vacio', required=True)
    parser.add_argument("sexe", type=str, help='Este campo no puede estar vacio', required=True)
    parser.add_argument("admspecialidad_id", type=int, help='Este campo no puede estar vacio', required=False)
    parser.add_argument("sucursal_id", type=int, help='Este campo no puede estar vacio', required=True)
    parser.add_argument("estado", type=bool, help='Este campo no puede estar vacio', required=False)

    @jwt_required()
    def get(self, id):
        if current_identity.super_admin == True or current_identity.admin_hospital == True:
            medico = MedicoModel.find_by_id(id)
            if medico:
                return medico.json()
            return {"message": "Medico not found"}
        return {"message": "You do not have authorization"}, 401

    @jwt_required()
    def post(self):
        data = MedicoResoure.parser.parse_args()
        if current_identity.super_admin == True or current_identity.admin_hospital == True:

            if MedicoModel.find_by_codigo(data["codigo"]):
                return {"message": "An usuario with name '{}' already exists".format(data['codigo'])}, 400

            if MedicoModel.find_by_cedula(data["cedula"]):
                return {"message": "An usuario with name '{}' already exists".format(data['cedula'])}, 400

            sucursal = MedicoModel(data['codigo'], data['cedula'], data['nombre'], data['apellidos']
                                   , data['telefono'], data['sexe'], data['admspecialidad_id'],
                                   data['sucursal_id'], data['estado'])

            try:
                sucursal.save_to_db()
            except:
                return {"message": "An error occured inserting the medico."}, 500

            return sucursal.json(), 201
        else:
            return {"message": "You do not have authorization"}, 401

    @jwt_required()
    def put(self, id):

        if current_identity.super_admin == True or current_identity.admin_hospital == True:
            user = MedicoModel.find_by_id(id)
            data = MedicoResoure.parser.parse_args()
            if user:
                user.codigo = data['codigo']
                user.cedula = data['cedula']
                user.nombre = data['nombre']
                user.apellidos = data['apellidos']
                user.telefono = data['telefono']
                user.sexe = data['sexe']
                user.admspecialidad_id = data['admspecialidad_id']
                user.sucursal_id = data['sucursal_id']
                user.estado = data['estado']

            else:
                user = MedicoModel(id, **data)

            try:
                user.save_to_db()
            except:
                return {"error": True, "message": "Medico data is not Updated !!! Try again"}

            return user.json(), 200
        else:
            return {"message": "You do not have authorization"}, 401

    @jwt_required()
    def delete(self, id):
        if current_identity.super_admin == True or current_identity.admin_hospital == True:

            user = MedicoModel.find_by_id(id)
            if user:
                user.delete_from_db()
                return {'message': "user deleted"}, 200

            return {"message": 'Product not found'}, 404
        else:
            return {"message": "You do not have authorization"}, 401


class MedicoGetList(Resource):
    @jwt_required()
    def get(self):
        if current_identity.super_admin == True or current_identity.admin_hospital == True:
            medico = MedicoModel.query.all()
            return {"medicos": list(map(lambda x: x.json(), medico))}
        else:
            return {"message": "You don't have authorization"}, 401


class MedicoEspecialidadGetList(Resource):
    @jwt_required()
    def get(self):
        if current_identity.super_admin == True or current_identity.admin_hospital == True:
            especialidad = MedicoSpecialidadModel.query.all()
            return {"especialidad": list(map(lambda x: x.json(), especialidad))}
        else:
            return {"message": "You don't have authorization"}, 401


class HorarioGetList(Resource):
    @jwt_required()
    def get(self):
        if current_identity.super_admin == True or current_identity.admin_hospital == True:
            horarios = HorarioModel.query.all()
            return {"horarios": list(map(lambda x: x.json(), horarios))}
        else:
            return {"message": "You don't have authorization"}, 401

from datetime import datetime

from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity

from flask_jwt_extended import jwt_required as jwt_required_extend, get_jwt_identity

from models.appointment import AppointmanetModel
from models.clientela import UsuarioModel


class AppointAdmin(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("c", help="this field can not null")

    @jwt_required()
    def get(self):
        appoint = AppointmanetModel.query.all()
        if appoint:
            return {'appointement_list': list(map(lambda x: x.json(), appoint))}, 200

    @jwt_required()
    def delete(self, id):
        appoint = AppointmanetModel.find_by_id(id)
        if appoint:
            appoint.delete_from_db()
            return {"message": "appointements was deleted"}, 200
        return {"message": 'Appointement not found'}, 404


class AppointResour(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("reason_appoint", help="this field can not null")

    @jwt_required_extend
    def get(self):
        cliente_id = get_jwt_identity()
        user = UsuarioModel.find_by_id(cliente_id)
        if user.verificacion_email == True:
            appoint = AppointmanetModel.query.filter_by(cliente_id=cliente_id).all()
            if appoint:
                return {'client_appointement': list(map(lambda x: x.json(), appoint))}, 200
            return {"message": "appoint not found"}, 404
        else:
            return {"message": "Confirme youre Email"}, 401

    @jwt_required_extend
    def post(self):
        data = AppointResour.parser.parse_args()
        cliente_id = get_jwt_identity()
        user = UsuarioModel.find_by_id(cliente_id)
        if user.verificacion_email:
            appoint = AppointmanetModel(cliente_id, data["reason_appoint"])
            try:
                appoint.save_to_db()
            except:
                return {"message": "An error occured inserting the Appoitement."}, 500

            return appoint.json(), 201

        else:
            return {"message": "Confirme youre Email"}, 401


class AppoitmentList(Resource):
    @jwt_required()
    def get(self):
        if current_identity.super_admin == True or current_identity.admin_hospital == True:
            ap = AppointmanetModel.query.all()
            return {"appoitment_list": list(map(lambda x: x.json(), ap))}
        else:
            return {"message": "No tienes autorizacion"}, 401


class AppoitmentListById(Resource):
    @jwt_required()
    def get(self, id):
        if current_identity.super_admin == True or current_identity.admin_hospital == True:
            appoitment = AppointmanetModel.find_by_id(id)
            if appoitment:
                return appoitment.json()
            return {"message": "Cliente no encontrado"}, 404
        else:
            return {"message": "No eres administrador"}, 401

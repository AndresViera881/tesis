from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity

from models.examen import ExamenModel
from models.lentes_contacto import Opt_Lentes_Contacto
from models.opt_oftalmologia import OftalmologiaModel
from models.opt_ortoptica import OrtopticaModel
from models.opt_refraccion import RefraccionModel
from models.opt_refraccion_estado import RefraccionEstadoModel
from models.opt_refraccion_vision import RefraccionVisionModel


class ExamenResourc(Resource):
    parser = reqparse.RequestParser()
    # parser.add_argument("admusuario_id", type=str, help="Este campo es requerido", required=True)
    parser.add_argument("medico_id", type=int, help="Este campo es requerido", required=True)
    parser.add_argument("id_transaccion", type=int, help="Este campo es requerido", required=True)
    parser.add_argument("estado", type=bool, required=False, default=True)

    @jwt_required()
    def get(self, idT, id):
        if current_identity.super_admin == True or current_identity.admin_hospital == True:
            examens = ExamenModel.query.filter_by(id_transaccion=idT, paciente_id=id).all()
            if examens:
                return {'examens': list(map(lambda x: x.json(), examens))}, 200
            return {"message": "examen not found"}, 404
        else:
            return {"message": "You are not admin"}, 401

    @jwt_required()
    def post(self):
        data = ExamenResourc.parser.parse_args()
        if current_identity.super_admin == True or current_identity.admin_hospital == True:

            examen = ExamenModel(data['id_pacient'], data['medico_id'], data['id_transaccion'], data['estado'])
            try:
                examen.save_to_db()
            except:
                return {"message": "An error occured inserting the examen."}, 500

            return examen.json(), 201
        else:
            return {"message": "You don't have authorisation"}, 401

    @jwt_required()
    def put(self, id):
        if current_identity.super_admin == True or current_identity.admin_hospital == True:

            examen = ExamenModel.find_by_id(id)
            data = ExamenResourc.parser.parse_args()

            if examen:
                examen.admusuario_id = current_identity.getid()
                examen.paciente_id = data['paciente_id']
                examen.id_transaccion = data['id_transaccion']
                examen.paciente_id = data['fecha']
                examen.paciente_id = data['estado']
            else:
                examen = ExamenModel(id, **data)

            try:
                examen.save_to_db()
            except:
                return {"message": "An error occured update the Examen"}

            return examen.json()
        else:
            return {"message": "You don't have authorisation"}, 401

    @jwt_required()
    def delete(self, id):
        if current_identity.super_admin == True or current_identity.admin_hospital == True:
            examen = ExamenModel.find_by_id(id)
            oftamologia = OftalmologiaModel.find_by_examen_id(id)
            ortoptica = OrtopticaModel.find_by_examen_id(id)
            lent_contento = Opt_Lentes_Contacto.find_by_examen_id(id)
            refraccion = RefraccionModel.find_by_examen_id(id)
            refraccion_estado = RefraccionEstadoModel.find_by_examen_id(id)
            refraccion_vision = RefraccionVisionModel.find_by_examen_id(id)
            if examen:
                if oftamologia:
                    oftamologia.delete_from_db()
                elif ortoptica:
                    ortoptica.delete_from_db()
                elif lent_contento:
                    lent_contento.delete_from_db()
                else:
                    refraccion_estado.delete_from_db()
                    refraccion_vision.delete_from_db()
                    refraccion.delete_from_db()
                examen.delete_from_db()
                return {'message': "Examen deleted"}

            return {"message": 'Examen not found'}, 404
        else:
            return {"message": "You don't have authorisation"}, 401


class ExamenList(Resource):
    @jwt_required()
    def get(self):
        if current_identity.super_admin == True or current_identity.admin_hospital == True:
            examens = ExamenModel.query.all()
            return {'examens': list(map(lambda x: x.json(), examens))}, 200
        else:
            return {"message": "You don't have authorisation"}, 401

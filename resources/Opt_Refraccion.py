from datetime import datetime

from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity

from models.examen import ExamenModel
from models.opt_diagnostico import Opt_Diagnostico
from models.opt_refraccion import RefraccionModel
from models.opt_refraccion_estado import RefraccionEstadoModel
from models.opt_refraccion_tipo_estado import RefraccionTipoEstadoModel
from models.opt_refraccion_vision import RefraccionVisionModel


class OptRefracResource(Resource):
    parse = reqparse.RequestParser()

    # parse.add_argument("paciente_id", type=str, required=True)
    parse.add_argument("medico_id", type=int, help="completez ce champ", required=True)
    parse.add_argument("id_transaccion", type=int, required=True)
    parse.add_argument("estado", type=bool, default=False)

    parse.add_argument("finalOjoDerecho", type=str, help="completez ce champ")
    parse.add_argument("puntajeFinalOjoDerecho", type=str, help="completez ce champ")
    parse.add_argument("finalOjoIzquierdo", type=str, help="completez ce champ")
    parse.add_argument("puntajeFinalOjoIzquierdo", type=str, help="completez ce champ")
    parse.add_argument("finalAdd", type=str, help="completez ce champ")
    parse.add_argument("puntajeFinalAdd", type=str, help="completez ce champ")
    parse.add_argument("titMus", type=float, help="completez ce champ")
    parse.add_argument("ishihara", type=str, help="completez ce champ")
    parse.add_argument("AmslerOD", type=str, help="completez ce champ")
    parse.add_argument("AmslerOI", type=str, help="completez ce champ")
    parse.add_argument("dp", type=str, help="completez ce champ", )
    parse.add_argument("diagnostico", type=str, help="completez ce champ")
    parse.add_argument("diagnostico1", type=str, help="completez ce champ")
    parse.add_argument("diagnostico2", type=str, help="completez ce champ")
    parse.add_argument("diagnostico3", type=str, help="completez ce champ")
    parse.add_argument("tratamiento", type=str, help="completez ce champ")

    parse.add_argument('vlOjoDerechoSC', type=str, required=True, help='This field cannot be blank')  # 1
    parse.add_argument('vlOjoIzquierdoSC', type=str, required=True, help='This field cannot be blank')  # 2
    parse.add_argument('vlOjoDerechoCC', type=str, required=True, help='This field cannot be blank')  # 3
    parse.add_argument('vlOjoIzquierdoCC', type=str, required=True, help='This field cannot be blank')  # 4
    parse.add_argument('vpOjoDerechoSC', type=str, required=True, help='This field cannot be blank')  # 5
    parse.add_argument('vpOjoIzquierdoSC', type=str, required=True, help='This field cannot be blank')  # 6
    parse.add_argument('vpOjoDerechoCC', type=str, required=True, help='This field cannot be blank')  # 7
    parse.add_argument('vpOjoIzquierdoCC', type=str, required=True, help='This field cannot be blank')  # 8
    parse.add_argument('rxOjoDerecho', type=str, required=True, help='This field cannot be blank')  # 9
    parse.add_argument('rxOjoIzquierdo', type=str, required=True, help='This field cannot be blank')  # 10
    parse.add_argument('qtOjoDerecho', type=str, required=True, help='This field cannot be blank')  # 11
    parse.add_argument('qtOjoIzquierdo', type=str, required=True, help='This field cannot be blank')  # 12
    parse.add_argument('atrOjoDerecho', type=str, required=True, help='This field cannot be blank')  # 13
    parse.add_argument('atrOjoIzquierdo', type=str, required=True, help='This field cannot be blank')  # 14
    parse.add_argument('estOD', type=str, required=True, help='This field cannot be blank')
    parse.add_argument('cylOD', type=str, required=True, help='This field cannot be blank')
    parse.add_argument('ejeOD', type=str, required=True, help='This field cannot be blank')
    parse.add_argument('addOD', type=str, required=True, help='This field cannot be blank')
    parse.add_argument('estOI', type=str, required=True, help='This field cannot be blank')
    parse.add_argument('cylOI', type=str, required=True, help='This field cannot be blank')
    parse.add_argument('ejeOI', type=str, required=True, help='This field cannot be blank')
    parse.add_argument('addOI', type=str, required=True, help='This field cannot be blank')

    parse.add_argument("tipo_estado_id", type=int, help="completez ce champ")
    parse.add_argument("ojoDerecho", type=str, help="completez ce champ")
    parse.add_argument("ojoIzquierdo", type=str, help="completez ce champ")

    @jwt_required()
    def post(self, id_pacient):
        data = OptRefracResource.parse.parse_args()
        if current_identity.super_admin == True or current_identity.admin_hospital == True:

            examen = ExamenModel(id_pacient, data['medico_id'], data['id_transaccion'], data['estado'])

            try:
                examen.save_to_db()
            except:
                return {"message": "An error occured inserting the examen."}, 500

            id_examen = examen.getIdExm()

            opt_refraccion = RefraccionModel(id_examen, data["finalOjoDerecho"], data["puntajeFinalOjoDerecho"],
                                             data["finalOjoIzquierdo"], data["puntajeFinalOjoIzquierdo"],
                                             data["finalAdd"], data["puntajeFinalAdd"], data["titMus"],
                                             data["ishihara"], data["AmslerOD"], data["AmslerOI"],
                                             data["dp"], data["diagnostico"], data["diagnostico1"],
                                             data["diagnostico2"], data["diagnostico3"], data["tratamiento"])

            opt_refraccionvision = RefraccionVisionModel(id_examen, data["vlOjoDerechoSC"], data["vlOjoIzquierdoSC"],
                                                         data["vlOjoDerechoCC"], data["vlOjoIzquierdoCC"],
                                                         data["vpOjoDerechoSC"], data["vpOjoIzquierdoSC"],
                                                         data["vpOjoDerechoCC"], data["vpOjoIzquierdoCC"],
                                                         data["rxOjoDerecho"], data["rxOjoIzquierdo"],
                                                         data["qtOjoDerecho"], data["qtOjoIzquierdo"],
                                                         data["atrOjoDerecho"], data["atrOjoIzquierdo"],
                                                         data["estOD"], data["cylOD"], data["ejeOD"],
                                                         data["addOD"], data["estOI"], data["cylOI"],
                                                         data["ejeOI"], data["addOI"])

            opt_refreccioestado = RefraccionEstadoModel(id_examen, data["tipo_estado_id"],
                                                        data["ojoDerecho"], data["ojoIzquierdo"])

            try:
                opt_refraccionvision.save_to_db()
                opt_refraccion.save_to_db()
                opt_refreccioestado.save_to_db()

            except:
                return {"message": "An error occured inserting the examen."}, 500
            return {"message": " Refraccion is created success"}, 201
        else:
            return {"message": "You don't have authorisation"}, 401

    @jwt_required()
    def put(self, id):
        if current_identity.super_admin == True or current_identity.admin_hospital == True:

            refraccion = RefraccionModel.find_by_examen_id(id)
            refraccion_vision = RefraccionVisionModel.find_by_examen_id(id)
            refraccion_estado = RefraccionEstadoModel.find_by_examen_id(id)
            data = OptRefracResource.parse.parse_args()

            if refraccion:
                refraccion.finalOjoDerecho = data["finalOjoDerecho"]
                refraccion.puntajeFinalOjoDerecho = data["puntajeFinalOjoDerecho"]
                refraccion.finalOjoIzquierdo = data["finalOjoIzquierdo"]
                refraccion.puntajeFinalOjoIzquierdo = data["puntajeFinalOjoIzquierdo"]
                refraccion.finalAdd = data["finalAdd"]
                refraccion.puntajeFinalAdd = data["puntajeFinalAdd"]
                refraccion.titMus = data["titMus"]
                refraccion.ishihara = data["ishihara"]
                refraccion.AmslerOD = data["AmslerOD"]
                refraccion.AmslerOI = data["AmslerOI"]
                refraccion.dp = data["dp"]
                refraccion.diagnostico = data["diagnostico"]
                refraccion.diagnostico1 = data["diagnostico1"]
                refraccion.diagnostico2 = data["diagnostico2"]
                refraccion.diagnostico3 = data["diagnostico3"]
                refraccion.tratamiento = data["tratamiento"]

                refraccion_vision.vlOjoDerechoSC = data["vlOjoDerechoSC"]
                refraccion_vision.vlOjoIzquierdoSC = data["vlOjoIzquierdoSC"]
                refraccion_vision.vlOjoDerechoCC = data["vlOjoDerechoCC"]
                refraccion_vision.vlOjoIzquierdoCC = data["vlOjoIzquierdoCC"]
                refraccion_vision.vpOjoDerechoSC = data["vpOjoDerechoSC"]
                refraccion_vision.vpOjoIzquierdoSC = data["vpOjoIzquierdoSC"]
                refraccion_vision.vpOjoDerechoCC = data["vpOjoDerechoCC"]
                refraccion_vision.vpOjoIzquierdoCC = data["vpOjoIzquierdoCC"]
                refraccion_vision.rxOjoDerecho = data["rxOjoDerecho"]
                refraccion_vision.rxOjoIzquierdo = data["rxOjoIzquierdo"]
                refraccion_vision.qtOjoDerecho = data["qtOjoDerecho"]
                refraccion_vision.qtOjoIzquierdo = data["qtOjoIzquierdo"]
                refraccion_vision.atrOjoDerecho = data["atrOjoDerecho"]
                refraccion_vision.atrOjoIzquierdo = data["atrOjoIzquierdo"]
                refraccion_vision.estOD = data["estOD"]
                refraccion_vision.cylOD = data["cylOD"]
                refraccion_vision.ejeOD = data["ejeOD"]
                refraccion_vision.addOD = data["addOD"]
                refraccion_vision.estOI = data["estOI"]
                refraccion_vision.cylOI = data["cylOI"]
                refraccion_vision.ejeOI = data["ejeOI"]
                refraccion_vision.addOI = data["addOI"]
                refraccion_estado.tipo_estado_id = data["tipo_estado_id"]
                refraccion_estado.ojoDerecho = data["ojoDerecho"]
                refraccion_estado.ojoIzquierdo = data["ojoIzquierdo"]
            else:
                refraccion = RefraccionModel(id, **data)
                refraccion_vision = RefraccionVisionModel(id, **data)
                refraccion_estado = RefraccionEstadoModel(id, **data)

            try:
                refraccion.save_to_db()
                refraccion_vision.save_to_db()
                refraccion_estado.save_to_db()
            except:
                return {"message": "An error occured update the Examen"}

            return {"message": "Examen Update success"}, 200
        else:
            return {"message": "You don't have authorisation"}, 401


class RefraccionEstadoRessource(Resource):
    def get(self):
        opt_refraccion_tipoEstadoModel = RefraccionTipoEstadoModel.query.all()
        return {'refraccion_estado': list(map(lambda x: x.json(), opt_refraccion_tipoEstadoModel))}, 200


class Opt_DiagnosticoRessourceList(Resource):
    def get(self):
        opt_refraccion = Opt_Diagnostico.query.all()
        return {'diagnostico': list(map(lambda x: x.json(), opt_refraccion))}, 200

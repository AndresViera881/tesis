from flask_jwt import jwt_required, current_identity
from flask_restful import Resource, reqparse

from models.examen import ExamenModel
from models.lentes_contacto import Opt_Lentes_Contacto


class LenteContResource(Resource):
    parse = reqparse.RequestParser()

    parse.add_argument("medico_id", type=int, help="completez ce champ", required=True)
    parse.add_argument("id_transaccion", type=int, required=True)
    parse.add_argument("estado", type=bool, default=False)

    parse.add_argument("examenExternoOjoDerecho", type=str, help="completez ce champ")
    parse.add_argument("examenExternoOjoIzquierdo", type=str, help="completez ce champ")
    parse.add_argument("topografiaOjoDerecho", type=str, help="completez ce champ")
    parse.add_argument("topografiaOjoIzquierdo", type=str, help="completez ce champ")
    parse.add_argument("but", type=str, help="completez ce champ")
    parse.add_argument("schirmer", type=str, help="completez ce champ")
    parse.add_argument("curvaFinalOD", type=str, help="completez ce champ")
    parse.add_argument("poderFinalOD", type=str, help="completez ce champ")
    parse.add_argument("diametroFinalOD", type=str, help="completez ce champ")
    parse.add_argument("materialFinalOD", type=str, help="completez ce champ")
    parse.add_argument("disenoFinalOD", type=str, help="completez ce champ")
    parse.add_argument("curvaFinalOI", type=str, help="completez ce champ")
    parse.add_argument("poderFinalOI", type=str, help="completez ce champ")
    parse.add_argument("diametroFinalOI", type=str, help="completez ce champ")
    parse.add_argument("materialFinalOI", type=str, help="completez ce champ")
    parse.add_argument("disenoFinalOI", type=str, help="completez ce champ")

    @jwt_required()
    def post(self, id_pacient):
        data = LenteContResource.parse.parse_args()
        if current_identity.super_admin == True or current_identity.admin_hospital == True:

            examen = ExamenModel(id_pacient, data['medico_id'], data['id_transaccion'], data['estado'])
            try:
                examen.save_to_db()
            except:
                return {"message": "An error occured inserting the examen."}, 500

            id_examen = examen.getIdExm()

            opt_lente_contacto = Opt_Lentes_Contacto(id_examen, data["examenExternoOjoDerecho"],
                                                     data["examenExternoOjoIzquierdo"],
                                                     data["topografiaOjoDerecho"], data["topografiaOjoIzquierdo"],
                                                     data["but"], data["schirmer"],
                                                     data["curvaFinalOD"], data["poderFinalOD"],
                                                     data["diametroFinalOD"], data["materialFinalOD"],
                                                     data["disenoFinalOD"], data["curvaFinalOI"],
                                                     data["poderFinalOI"], data["diametroFinalOI"],
                                                     data["materialFinalOI"], data["disenoFinalOI"])

            try:
                opt_lente_contacto.save_to_db()
            except:
                return {"message": "An error occured inserting the examen."}, 500
            return {"message": " Oftamologia is created success"}, 201
        else:
            return {"message": "You don't have authorisation"}, 401

    @jwt_required()
    def put(self, id):
        if current_identity.super_admin == True or current_identity.admin_hospital == True:

            lente_contatcto = Opt_Lentes_Contacto.find_by_examen_id(id)
            data = LenteContResource.parse.parse_args()

            if lente_contatcto:
                lente_contatcto.examenExternoOjoDerecho = data["examenExternoOjoDerecho"]
                lente_contatcto.examenExternoOjoIzquierdo = data["examenExternoOjoIzquierdo"]
                lente_contatcto.topografiaOjoDerecho = data["topografiaOjoDerecho"]
                lente_contatcto.topografiaOjoIzquierdo = data["topografiaOjoIzquierdo"]
                lente_contatcto.but = data["but"]
                lente_contatcto.schirmer = data["schirmer"]
                lente_contatcto.curvaFinalOD = data["curvaFinalOD"]
                lente_contatcto.poderFinalOD = data["poderFinalOD"]
                lente_contatcto.diametroFinalOD = data["diametroFinalOD"]
                lente_contatcto.materialFinalOD = data["materialFinalOD"]
                lente_contatcto.disenoFinalOD = data["disenoFinalOD"]
                lente_contatcto.curvaFinalOI = data["curvaFinalOI"]
                lente_contatcto.poderFinalOI = data["poderFinalOI"]
                lente_contatcto.diametroFinalOI = data["diametroFinalOI"]
                lente_contatcto.materialFinalOI = data["materialFinalOI"]
                lente_contatcto.disenoFinalOI = data["disenoFinalOI"]

            else:
                lente_contatcto = Opt_Lentes_Contacto(id, **data)

            try:
                lente_contatcto.save_to_db()
            except:
                return {"message": "An error occured update the Examen"}

            return lente_contatcto.json()
        else:
            return {"message": "You don't have authorisation"}, 401

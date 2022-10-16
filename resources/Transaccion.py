from flask_jwt import jwt_required, current_identity
from flask_restful import Resource, reqparse
from models.transaccion import TransaccionModel


class TransaccionRessource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("transaccion", type=str, help="Este campo es requerido", required=True)
    parser.add_argument("stado", type=bool, help="Este campo es requerido", required=True)

    def get(self):
        transaccion = TransaccionModel.query.all()
        return {'examens': list(map(lambda x: x.json(), transaccion))}, 200

    @jwt_required()
    def post(self):
        data = TransaccionRessource.parser.parse_args()
        if current_identity.super_admin == True or current_identity.admin_hospital == True:

            examen = TransaccionModel(data['transaccion'], data['estado'])
            try:
                examen.save_to_db()
            except:
                return {"message": "An error occured inserting the transaccion."}, 500

            return examen.json(), 201
        else:
            return {"message": "You don't have authorisation"}, 401

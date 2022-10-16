from flask_restful import Resource, reqparse
from models.sucursal import SucursalModel
from flask_jwt import jwt_required, current_identity


class SucursalList(Resource):
    def get(self):
        sucursal = SucursalModel.query.all()
        return {"sucursals": list(map(lambda x: x.json(), sucursal))}, 200

    def getById(self, id):
        sucursal = SucursalModel.find_by_id(id)
        if sucursal:
            return sucursal.json()
        return {"message": "Sucursal no encontrada"}, 404


class SucursalRes(Resource):
    parse = reqparse.RequestParser()
    parse.add_argument("nombre", type=str, help="Este campo es requerido", required=True)
    parse.add_argument("direccion", type=str, help="Este campo es requerido", required=True)
    parse.add_argument("estado", type=bool, help="Este campo es requerido", required=False)

    def get(self, id):
        sucursal = SucursalModel.find_by_id(id)

        if sucursal:
            return sucursal.json()
        return {"message": "Sucursal not found"}, 404

    def post(self):
        data = SucursalRes.parse.parse_args()

        if SucursalModel.find_by_nombre(data["nombre"]):
            return {"message": "El nombre de la sucursal {} ya existe".format(data['nombre'])}, 400
        sucursal = SucursalModel(data['nombre'], data['direccion'], data['estado'])

        try:
            sucursal.save_to_db()
        except:
            return {"message": "An error occured inserting the sucursal."}, 500

        return sucursal.json(), 201

    def put(self, id):
        sucursal = SucursalModel.find_by_id(id)
        data = SucursalRes.parse.parse_args()

        if sucursal:
            sucursal.nombre = data['nombre']
            sucursal.direccion = data['direccion']
            sucursal.estado = data['estado']

        else:
            sucursal = SucursalModel(id, **data)
        try:
            sucursal.save_to_db()
        except:
            return {"message": "Error al actualizar la sucursal"}

        return sucursal.json(), 200

    def delete(self, id):
        sucursal = SucursalModel.find_by_id(id)
        if sucursal:
            sucursal.delete_from_db()
            return {'message': "Sucursal eliminada"}
        return {"message": 'Sucursal no encontrada'}, 404

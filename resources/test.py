"""from flask_restful import Resource, reqparse

from models.opt_diagnostico import Test1, Test2


class Test(Resource):
    parse = reqparse.RequestParser()
    parse.add_argument("titre1", type=str, help="completez ce champ", required=True)
    parse.add_argument("donne1", type=str, help="completez ce champ", required=True)
    parse.add_argument("titre2", type=str, help="completez ce champ", required=True)
    parse.add_argument("donne2", type=str, help="completez ce champ", required=True)

    def get(self):
        examens = Test1.query.all()
        return {'examens': list(map(lambda x: x.json(), examens))}, 200

    def post(self):
        data = Test.parse.parse_args()

        test1 = Test1(data["titre1"],data["donne1"])
        test2 = Test2(data["titre2"], data["donne2"])

        try:
            test2.save_to_db()
            test1.save_to_db()
        except:
            return {"message": "An error occured inserting the examen."}, 500
        return {"message": "save to db"}
"""
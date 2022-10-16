# from flask_restful import Resource
# from flask_bcrypt import Bcrypt
# from flask import request, jsonify
# import jwt
# import datetime
# from app import app
#
# from models.clientela import UsuarioModel
#
# bc = Bcrypt()
#
#
# class LoginCl(Resource):
#     def post(self):
#         auth = request.authorization
#
#         if not auth or not auth.username or not auth.password:
#             return {"message": "error"}, 401
#
#         user = UsuarioModel.query.filter_by(email=auth.username).first()
#
#         if bc.check_password_hash(user.password, auth.password):
#             token = jwt.encode(
#                 {'public_id': user.public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
#                 app.config['SECRET_KEY'])
#             return jsonify({'token': token.decode('UTF-8')})
#
#         return {"message": "error"}, 401

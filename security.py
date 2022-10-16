from models.adm import AdminUsuario
from flask_bcrypt import Bcrypt

bc = Bcrypt()


def authenticate(username, password):
    user = AdminUsuario.find_by_correo(username)
    if user and user.check_password(password):
        return user
    else:
        return None


def identity(payload):
    user_id = payload['identity']
    return AdminUsuario.find_by_id(user_id)


def make_payload(identity):
    return {'user_id': identity.id}

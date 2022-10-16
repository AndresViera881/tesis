from datetime import timedelta, datetime, timezone

from flask_jwt_extended import JWTManager, create_access_token, set_access_cookies, get_jwt_identity, get_raw_jwt
from itsdangerous import URLSafeTimedSerializer

from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
from flask_migrate import Migrate
from flask_jwt import JWT
from flask_bcrypt import Bcrypt

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from sqlalchemy import create_engine
from werkzeug.utils import redirect

from db import db
from models.appointment import AppointmanetModel
from models.clientela import UsuarioModel, TblCitas
from models.examen import ExamenModel
from models.lentes_contacto import Opt_Lentes_Contacto
from models.medico import MedicoModel, MedicoSpecialidadModel, MedicoHorario, HorarioModel
from models.opt_diagnostico import Opt_Diagnostico
from models.opt_oftalmologia import OftalmologiaModel
from models.opt_ortoptica import OrtopticaModel
from models.opt_refraccion import RefraccionModel
from models.opt_refraccion_estado import RefraccionEstadoModel
from models.opt_refraccion_tipo_estado import RefraccionTipoEstadoModel
from models.opt_refraccion_vision import RefraccionVisionModel
from models.opt_tipo_test_dem import OptTipoTestDemModel

from models.paciente import PacienteModel
from models.paciente_remitido import pacienteRemitidoModel
from models.sucursal import SucursalModel
from models.adm import AdminUsuario
from models.test_adicional_tipo import TestAdicionalTipoModel
from models.transaccion import TransaccionModel
from resources.Adm import AdmResoure, AdmUsuarioUpdat, AdmResoureList, AdmResoureListById
from resources.Appointement import AppointResour, AppoitmentList, AppoitmentListById
from resources.Clientela import ClienteResours, CitaList, CitasResour, ClientelaList, confirma_email, LoginClient, \
    CitaListById
from resources.Examen import ExamenResourc, ExamenList
from resources.Lente_Contento import LenteContResource
from resources.Medico import MedicoGetList, MedicoResoure, MedicoEspecialidadGetList, HorarioGetList
from resources.Opt_Refraccion import OptRefracResource, Opt_DiagnosticoRessourceList, RefraccionEstadoRessource
from resources.Opt_oftamologia import Opt0ftamologia
from resources.Opt_ortoptica import OrtopticaTipoRessource, OptOrtopeticResource, OrtopticaTipoTestDemRessource, \
    OptOrtopticaPutRessource
from resources.Paciente import PacienteLists, PacientResource
from resources.Sucursal import SucursalList, SucursalRes
from resources.Transaccion import TransaccionRessource
from security import authenticate, identity

app = Flask(__name__)

app.config['SECRET_KEY'] = '035088966eda4454b5016d817708652a'
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:andresviera@localhost/flask_tesis_final"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://kjjixvizbshbqc:0af37376f4df41d43ced2f0190148db977e727776aea42d77c2af2eab41c0575@ec2-44-199-143-43.compute-1.amazonaws.com:5432/d2dlel21r1j8ac"
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], pool_pre_ping=True, pool_size=30, max_overflow=120)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['JWT_SECRET_KEY'] = '035088966eda4454b5016d817708A25'
app.config['JWT_DEFAULT_REALM'] = True
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=24)
app.config['JWT_LEEWAY'] = timedelta(seconds=1209600)
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1209600)
# app.config['JWT_NOT_BEFORE_DELTA'] = timedelta(seconds=1209600)
app.config['JWT_AUTH_URL_RULE'] = '/login'

api = Api(app)

CORS(app)
bc = Bcrypt()


@app.before_first_request
def create_tables():
    db.create_all()


@app.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_raw_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            set_access_cookies(response, access_token)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original respone
        return response


Jwt = JWT(app, authenticate, identity)
jwtexted = JWTManager(app)

#
# admin request__________________________________
api.add_resource(AdmResoureList, '/api/admin/lists')
api.add_resource(AdmResoureListById, '/api/admin/<int:id>')
api.add_resource(AdmResoure, '/api/admin/', '/api/admin/<int:id>')
api.add_resource(AdmUsuarioUpdat, '/api/admin/update/<int:id>')

# patient and examens request_____________________
api.add_resource(ExamenResourc, '/api/examen/', '/api/examen/<int:id>', '/api/examen/<int:idT>/<int:id>')
api.add_resource(ExamenList, '/api/examen/lists')
api.add_resource(PacienteLists, '/api/pacientes/lists')
api.add_resource(PacientResource, '/api/paciente/', '/api/paciente/<int:id>', '/api/pacienteById/<int:id>')
api.add_resource(TransaccionRessource, '/api/transaccion/', '/api/transaccion/<int:id>')
# Sucursal request
api.add_resource(SucursalList, '/api/sucursal/lists')
api.add_resource(SucursalRes, '/api/sucursal/<int:id>', '/api/sucursal')

# Medico request
api.add_resource(MedicoGetList, '/api/medico/lists')
api.add_resource(MedicoEspecialidadGetList, '/api/especialidad/lists/')
api.add_resource(MedicoResoure, '/api/medico/', '/api/medico/<int:id>')

# Diagnostico request
api.add_resource(Opt_DiagnosticoRessourceList, '/api/diagnostico/lists')

# Reffraccion request
api.add_resource(OptRefracResource, '/api/refraccion/<int:id_pacient>', '/api/refraccion/<int:id>')
api.add_resource(RefraccionEstadoRessource, '/api/refraccionestado/lists')

# Oftamologia request
api.add_resource(Opt0ftamologia, '/api/oftamologia/<int:id_pacient>', '/api/oftamologia/<int:id>', '/api/oftamologiaById/<int:id>')

# Ortoptical request
api.add_resource(OrtopticaTipoTestDemRessource, '/api/ortopticaTestDem/lists')
api.add_resource(OrtopticaTipoRessource, '/api/ortopticaTipo/lists')
api.add_resource(OptOrtopeticResource, '/api/ortoptica/<int:paciente_id>/<int:transaccion_id>',
                 '/api/ortopticaById/<int:id>')
api.add_resource(OptOrtopticaPutRessource, '/api/ortoptica/<int:id>')
# Lente Conten request
api.add_resource(LenteContResource, '/api/lentecontento/<int:id_pacient>', '/api/lentecontento/<int:id>')

# clientela request__________________________________
api.add_resource(ClienteResours, '/api/client/post')
api.add_resource(confirma_email, '/auth/confirmar_email/<string:token>/<string:correo>')
# api.add_resource(Logincl, '/api/login/', '/api/login/<public_id>')
api.add_resource(LoginClient, '/api/login/', '/api/login/<public_id>')

# cita requeste___________________________________
api.add_resource(ClientelaList, '/api/client/lists')
api.add_resource(AppointResour, '/api/appointment/')
api.add_resource(AppoitmentList, '/api/appointment/list')
api.add_resource(AppoitmentListById, '/api/appointmentById/<int:id>')
api.add_resource(CitasResour, '/api/cita/', '/api/cita/<int:id>')
api.add_resource(CitaList, '/api/cita/lists')
api.add_resource(CitaListById, '/api/cita/<int:id>')
api.add_resource(HorarioGetList, '/api/horarios/lists')

migrate = Migrate(app, db)

admin = Admin(app, name='Tesis admin', template_mode='bootstrap3')

admin.add_view(ModelView(PacienteModel, db.session))
admin.add_view(ModelView(SucursalModel, db.session))
admin.add_view(ModelView(AdminUsuario, db.session))
admin.add_view(ModelView(MedicoModel, db.session))
admin.add_view(ModelView(MedicoSpecialidadModel, db.session))
admin.add_view(ModelView(MedicoHorario, db.session))
admin.add_view(ModelView(HorarioModel, db.session))
admin.add_view(ModelView(ExamenModel, db.session))
admin.add_view(ModelView(OftalmologiaModel, db.session))
admin.add_view(ModelView(RefraccionTipoEstadoModel, db.session))
admin.add_view(ModelView(RefraccionVisionModel, db.session))
admin.add_view(ModelView(RefraccionModel, db.session))
admin.add_view(ModelView(Opt_Lentes_Contacto, db.session))
admin.add_view(ModelView(OrtopticaModel, db.session))
admin.add_view(ModelView(RefraccionEstadoModel, db.session))
admin.add_view(ModelView(pacienteRemitidoModel, db.session))
admin.add_view(ModelView(TestAdicionalTipoModel, db.session))
admin.add_view(ModelView(TransaccionModel, db.session))
admin.add_view(ModelView(OptTipoTestDemModel, db.session))
admin.add_view(ModelView(Opt_Diagnostico, db.session))
admin.add_view(ModelView(AppointmanetModel, db.session))
admin.add_view(ModelView(UsuarioModel, db.session))
admin.add_view(ModelView(TblCitas, db.session))

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

if __name__ == "__main__":
    migrate.init_app(app, db)
    db.init_app(app)
    app.run()

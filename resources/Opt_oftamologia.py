import werkzeug
import os
import uuid
from werkzeug.utils import secure_filename
from flask_jwt import jwt_required, current_identity
from flask_restful import Resource, reqparse

from models.examen import ExamenModel
from models.opt_oftalmologia import OftalmologiaModel


class Opt0ftamologia(Resource):
    parse = reqparse.RequestParser()

    # parse.add_argument("paciente_id", type=str, required=True)
    parse.add_argument("medico_id", type=int, help="completez ce champ", required=False)
    parse.add_argument("id_transaccion", type=int, required=False)
    parse.add_argument("estado", type=bool, default=False)

    parse.add_argument("OftOjoDerecho", type=str)
    parse.add_argument("imagenOftOjoDerecho", type=werkzeug.datastructures.FileStorage, location='files')
    parse.add_argument("OftOjoIzquierdo", type=str)
    parse.add_argument("imagenOftOjoIzquierdo", type=werkzeug.datastructures.FileStorage, location='files')
    parse.add_argument("BioOjoDerecho", type=str)
    parse.add_argument("imagenBioOjoDerecho", type=werkzeug.datastructures.FileStorage, location='files')
    parse.add_argument("BioOjoIzquierdo", type=str)
    parse.add_argument("imagenBioOjoIzquierdo", type=werkzeug.datastructures.FileStorage, location='files')
    parse.add_argument("tratamiento", type=str)
    parse.add_argument("diagnostico", type=str)
    parse.add_argument("diagnostico1", type=str)
    parse.add_argument("diagnostico2", type=str)
    parse.add_argument("diagnostico3", type=str)
    parse.add_argument("vlOjoDerechoSC", type=str)
    parse.add_argument("vlOjoIzquierdoSC", type=str)
    parse.add_argument("vlOjoDerechoCC", type=str)
    parse.add_argument("vlOjoIzquierdoCC", type=str)
    parse.add_argument("consulta", type=str)

    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'jfif'])

    def allowed_file(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in self.ALLOWED_EXTENSIONS

    @jwt_required()
    def post(self, id_pacient):
        data = Opt0ftamologia.parse.parse_args()
        print(data)
        imagenOftOjoDerecho = data['imagenOftOjoDerecho']
        imagenOftOjoIzquierdo = data['imagenOftOjoIzquierdo']
        imagenBioOjoDerecho = data['imagenBioOjoDerecho']
        imagenBioOjoIzquierdo = data['imagenBioOjoIzquierdo']
        if imagenOftOjoDerecho and self.allowed_file(imagenOftOjoDerecho.filename):
            filename_OftOjoDerecho = str(uuid.uuid4()) + '.' + imagenOftOjoDerecho.filename.rsplit('.', 1)[1].lower()
            filenames = secure_filename(imagenOftOjoDerecho.filename)
            imagenOftOjoDerecho.save(
                os.path.join(os.getcwd(), 'static', 'oftamologia', '', filename_OftOjoDerecho or filenames))
        else:
            return {"message": "no field"}

        if imagenOftOjoIzquierdo and self.allowed_file(imagenOftOjoIzquierdo.filename):
            filename_OftOjoIzquierdo = str(uuid.uuid4()) + '.' + imagenOftOjoIzquierdo.filename.rsplit('.', 1)[
                1].lower()
            filenames = secure_filename(imagenOftOjoIzquierdo.filename)
            imagenOftOjoIzquierdo.save(
                os.path.join(os.getcwd(), 'static', 'oftamologia', '', filename_OftOjoIzquierdo or filenames))
        else:
            return {"message": "no field"}

        if imagenBioOjoDerecho and self.allowed_file(imagenBioOjoDerecho.filename):
            filename_BioOjoDerecho = str(uuid.uuid4()) + '.' + imagenBioOjoDerecho.filename.rsplit('.', 1)[1].lower()
            filenames = secure_filename(imagenBioOjoDerecho.filename)
            imagenBioOjoDerecho.save(
                os.path.join(os.getcwd(), 'static', 'oftamologia', '', filename_BioOjoDerecho or filenames))
        else:
            return {"message": "no field"}

        if imagenBioOjoIzquierdo and self.allowed_file(imagenBioOjoIzquierdo.filename):
            filename_BioOjoIzquierdo = str(uuid.uuid4()) + '.' + imagenBioOjoIzquierdo.filename.rsplit('.', 1)[
                1].lower()
            filenames = secure_filename(imagenBioOjoIzquierdo.filename)
            imagenBioOjoIzquierdo.save(
                os.path.join(os.getcwd(), 'static', 'oftamologia', '', filename_BioOjoIzquierdo or filenames))
        else:
            return {"message": "no field"}

        if current_identity.super_admin == True or current_identity.admin_hospital == True:

            examen = ExamenModel(id_pacient, data['medico_id'], data['id_transaccion'], data['estado'])
            try:
                examen.save_to_db()
            except:
                return {"message": "An error occured inserting the examen."}, 500

            id_examen = examen.getIdExm()
            filenames_OftOjoDerecho = filename_OftOjoDerecho
            opt_oftamologia = OftalmologiaModel(id_examen, data["OftOjoDerecho"], filenames_OftOjoDerecho,
                                                data["OftOjoIzquierdo"], filename_OftOjoIzquierdo,
                                                data["BioOjoDerecho"], filename_BioOjoDerecho,
                                                data["BioOjoIzquierdo"], filename_BioOjoIzquierdo,
                                                data["tratamiento"], data["diagnostico"], data["diagnostico1"],
                                                data["diagnostico2"], data["diagnostico3"],
                                                data["vlOjoDerechoSC"], data["vlOjoIzquierdoSC"],
                                                data["vlOjoDerechoCC"], data["vlOjoIzquierdoCC"], data["consulta"])

            try:
                opt_oftamologia.save_to_db()
            except:
                return {"message": "An error occured inserting the examen."}, 500
            return {"message": " Oftamologia is created success"}, 201
        else:
            return {"message": "You don't have authorisation"}, 401

    @jwt_required()
    def put(self, id):
        data = Opt0ftamologia.parse.parse_args()

        imagenOftOjoDerecho = data['imagenOftOjoDerecho']
        imagenOftOjoIzquierdo = data['imagenOftOjoIzquierdo']
        imagenBioOjoDerecho = data['imagenBioOjoDerecho']
        imagenBioOjoIzquierdo = data['imagenBioOjoIzquierdo']

        if imagenOftOjoDerecho and self.allowed_file(imagenOftOjoDerecho.filename):
            filename_OftOjoDerecho = str(uuid.uuid4()) + '.' + \
                                     imagenOftOjoDerecho.filename_OftOjoDerecho.rsplit('.', 1)[1].lower()
            filenames = secure_filename(imagenOftOjoDerecho.filename_OftOjoDerecho)
            imagenOftOjoDerecho.save(
                os.path.join(os.getcwd(), 'static', 'oftamologia', '', filename_OftOjoDerecho or filenames))

        if imagenOftOjoIzquierdo and self.allowed_file(imagenOftOjoIzquierdo.filename):
            filename_OftOjoIzquierdo = str(uuid.uuid4()) + '.' + \
                                       imagenOftOjoIzquierdo.filename_OftOjoIzquierdo.rsplit('.', 1)[1].lower()
            filenames = secure_filename(imagenOftOjoIzquierdo.filename_OftOjoIzquierdo)
            imagenOftOjoIzquierdo.save(
                os.path.join(os.getcwd(), 'static', 'oftamologia', '', filename_OftOjoIzquierdo or filenames))

        if imagenBioOjoDerecho and self.allowed_file(imagenBioOjoDerecho.filename):
            filename_BioOjoDerecho = str(uuid.uuid4()) + '.' + \
                                     imagenBioOjoDerecho.filename_BioOjoDerecho.rsplit('.', 1)[1].lower()
            filenames = secure_filename(imagenBioOjoDerecho.filename_BioOjoDerecho)
            imagenBioOjoDerecho.save(
                os.path.join(os.getcwd(), 'static', 'oftamologia', '', filename_BioOjoDerecho or filenames))

        if imagenBioOjoIzquierdo and self.allowed_file(imagenBioOjoIzquierdo.filename):
            filename_BioOjoIzquierdo = str(uuid.uuid4()) + '.' + \
                                       imagenBioOjoIzquierdo.filename_BioOjoIzquierdo.rsplit('.', 1)[1].lower()
            filenames = secure_filename(imagenBioOjoIzquierdo.filename_BioOjoIzquierdo)
            imagenBioOjoIzquierdo.save(
                os.path.join(os.getcwd(), 'static', 'oftamologia', '', filename_BioOjoIzquierdo or filenames))

        if current_identity.super_admin == True or current_identity.admin_hospital == True:

            oftamologia = OftalmologiaModel.find_by_examen_id(id)

            if oftamologia:
                oftamologia.OftOjoDerecho = data["OftOjoDerecho"]
                oftamologia.filename_OftOjoDerecho = filename_OftOjoDerecho
                oftamologia.OftOjoIzquierdo = data["OftOjoIzquierdo"]
                oftamologia.filename_OftOjoIzquierdo = filename_OftOjoIzquierdo
                oftamologia.BioOjoDerecho = data["BioOjoDerecho"]
                oftamologia.filename_BioOjoDerecho = filename_BioOjoDerecho
                oftamologia.BioOjoIzquierdo = data["BioOjoIzquierdo"]
                oftamologia.filename_BioOjoIzquierdo = filename_BioOjoIzquierdo
                oftamologia.tratamiento = data["tratamiento"]
                oftamologia.diagnostico = data["diagnostico"]
                oftamologia.diagnostico1 = data["diagnostico1"]
                oftamologia.diagnostico2 = data["diagnostico2"]
                oftamologia.diagnostico3 = data["diagnostico3"]
                oftamologia.OftOjoDerecho = data["vlOjoDerechoSC"]
                oftamologia.vlOjoDerechoSC = data["vlOjoIzquierdoSC"]
                oftamologia.vlOjoDerechoCC = data["vlOjoDerechoCC"]
                oftamologia.vlOjoIzquierdoCC = data["vlOjoIzquierdoCC"]
                oftamologia.consulta = data["consulta"]

            else:
                oftamologia = OftalmologiaModel(id, **data)

            try:
                oftamologia.save_to_db()
            except:
                return {"message": "An error occured update the Examen"}

            return oftamologia.json()
        else:
            return {"message": "You don't have authorisation"}, 401

    @jwt_required()
    def get(self, id):
        if current_identity.super_admin == True or current_identity.admin_hospital == True:
            oftalmologiaById = OftalmologiaModel.find_by_examen_id(id)
            if oftalmologiaById:
                return oftalmologiaById.json()
            return {"message": "Oftalmologia not found"}, 404
        else:
            return {"message": "You are not admin"}, 401

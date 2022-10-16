from datetime import date, time, datetime
from flask_bcrypt import Bcrypt
from flask_jwt import current_identity

from db import db

bc = Bcrypt()


class UsuarioModel(db.Model):
    __tablename__ = "tbl_usuario"

    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    nombre = db.Column(db.String(50))
    apellidos = db.Column(db.String(50))
    cedula = db.Column(db.String(100), nullable=False)
    sexo = db.Column(db.String(10), nullable=False)
    direccion = db.Column(db.String(100), nullable=False)
    fecha_nacimiento = db.Column(db.Date, default=date.today())
    correo = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    verificacion_email = db.Column(db.Boolean, default=False)
    telefono = db.Column(db.String(13), nullable=False)

    def __init__(self, public_id, nombre, apellidos, cedula, sexo, direccion, fecha_nacimiento, correo, password,
                 telefono):
        self.public_id = public_id
        self.nombre = nombre
        self.apellidos = apellidos
        self.cedula = cedula
        self.sexo = sexo
        self.direccion = direccion
        self.fecha_nacimiento = fecha_nacimiento
        self.correo = correo
        self.password = password
        self.telefono = telefono

    def __str__(self):
        return f"id; {self.id}__ nombre: {self.nombre}__ usuario: {self.usuario}"

    def getId(self):
        return self.id

    def getpublic_id(self):
        return self.public_id

    def json(self):
        return {
            "id": self.id,
            "public_id": self.public_id,
            "nombre": self.nombre,
            "apellidos": self.apellidos,
            "correo": self.correo,
            "cedula": self.cedula,
            "sexo": self.sexo,
            "direccion": self.direccion,
            "fecha_nacimiento": str(self.fecha_nacimiento),
            "telefono": self.telefono,
        }

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_public_id(cls, public_id):
        return cls.query.filter_by(public_id=public_id).first()

    @classmethod
    def find_by_correo(cls, correo):
        return cls.query.filter_by(correo=correo).first()

    @classmethod
    def find_by_cedula(cls, cedula):
        return cls.query.filter_by(cedula=cedula).first()

    def check_password(self, password):
        """check hashed password."""
        return bc.check_password_hash(self.password, password)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


now = datetime.now()
current_time = now.time()


class TblCitas(db.Model):
    __tablename__ = "tbl_citas"

    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, default=date.today())
    hora = db.Column(db.TIMESTAMP, default=current_time)
    estado = db.Column(db.Boolean)

    cliente_id = db.Column(db.Integer, db.ForeignKey("tbl_usuario.id"))
    cliente_ = db.relationship("UsuarioModel", lazy=True)

    medico_id = db.Column(db.Integer, db.ForeignKey("tbl_medicos.id"))
    medico_ = db.relationship("MedicoModel", lazy=True)

    horario_id = db.Column(db.Integer, db.ForeignKey("tbl_horario.id"))
    horario_ = db.relationship("HorarioModel", lazy=True)

    admin_id = db.Column(db.Integer, db.ForeignKey("admin_usuarios.id"))
    admin_ = db.relationship("AdminUsuario", lazy=True)

    def __init__(self, fecha, hora, estado, cliente_id, medico_id, horario_id):
        self.admin_id = current_identity.getid()
        self.fecha = fecha
        self.hora = hora
        self.estado = estado
        self.cliente_id = cliente_id
        self.medico_id = medico_id
        self.horario_id = horario_id

    def __str__(self):
        return f"id; {self.id}__ cliente_id: {self.cliente_id}"

    def json(self):
        return {
            "fecha": str(self.fecha),
            "hora": str(self.hora),
            "estado": self.estado,
            "clientela": {
                "id": self.cliente_id,
                "public_id": self.cliente_.public_id,
                "nombre": self.cliente_.nombre,
                "apellidos": self.cliente_.apellidos,
                "cedula": self.cliente_.cedula,
                "sexo": self.cliente_.sexo,
                "direccion": self.cliente_.direccion,
                # "fecha_nacimiento": self.cliente_.fecha_nacimiento,
                "correo": self.cliente_.direccion,
                "password": self.cliente_.password
            },
            "medico": {
                "id": self.medico_id,
                "codigo": self.medico_.codigo,
                "cedula": self.medico_.cedula,
                "nombre": self.medico_.nombre,
                "apellidos": self.medico_.apellidos,
                "telefono": self.medico_.telefono,
                "sexe": self.medico_.sexe,

            },
            "horario": {
                "id": self.horario_id,
                "dia": self.horario_.dia,
                "horario_inicio": self.horario_.horario_inicio,
                "horario_fin": self.horario_.horario_fin

            }
        }

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_cliente_id(cls, cliente_id):
        return cls.query.filter_by(cliente_id=cliente_id).first()

    @classmethod
    def find_by_cliente_ids(cls, cliente_id):
        return cls.query.filter_by(cliente_id=cliente_id).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

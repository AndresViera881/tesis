from db import db
from flask_bcrypt import Bcrypt

bc = Bcrypt()


class AdminUsuario(db.Model):
    __tablename__ = "admin_usuarios"
    id = db.Column(db.Integer, primary_key=True)
    cedula = db.Column(db.String(13), unique=True)
    nombres = db.Column(db.String(200))
    apellidos = db.Column(db.String(200))
    correo = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))
    direccion = db.Column(db.String(250))
    telefono = db.Column(db.String(20))
    sexe = db.Column(db.String(15))
    admin_clientela = db.Column(db.Boolean, default=False)
    admin_hospital = db.Column(db.Boolean, default=True)
    super_admin = db.Column(db.Boolean, default=False)

    def __init__(self, cedula, nombres, apellidos, correo, password, direccion, telefono, sexe, admin_clientela,
                 admin_hospital, super_admin):
        self.cedula = cedula
        self.nombres = nombres
        self.apellidos = apellidos
        self.correo = correo
        self.password = password
        self.direccion = direccion
        self.telefono = telefono
        self.sexe = sexe
        self.admin_clientela = admin_clientela
        self.admin_hospital = admin_hospital
        self.super_admin = super_admin

    def __str__(self):
        return f"id: {self.id} cedula: {self.cedula} nombres: {self.nombres} apellidos:{self.apellidos} "

    def getid(self):
        return self.id

    def json(self):
        return {
            "id": self.id,
            "cedula": self.cedula,
            "nombres": self.nombres,
            "apellidos": self.apellidos,
            "correo": self.correo,
            "password": self.password,
            "direccion": self.direccion,
            "telefono": self.telefono,
            "sexe": self.sexe,
            "admin_clientela": self.admin_clientela,
            "admin_hospital": self.admin_hospital,
            "super_admin": self.super_admin,
        }

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

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

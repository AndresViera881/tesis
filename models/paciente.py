from datetime import datetime, date

from db import db


class PacienteModel(db.Model):
    __tablename__ = 'paciente'
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(100), unique=True)
    cedula = db.Column(db.String(13), unique=True)
    nombres = db.Column(db.String(250))
    apellidos = db.Column(db.String(250))
    fecha_nacimiento = db.Column(db.Date, default=date.today())
    correo = db.Column(db.String(150), unique=True)
    direccion = db.Column(db.String(250))
    ocupacion = db.Column(db.String(250))
    telefono = db.Column(db.String(10))
    estado = db.Column(db.Boolean, default=True)

    sucursal_id = db.Column(db.Integer, db.ForeignKey('sucursal.id'))
    sucursal = db.relationship('SucursalModel')

    observacion = db.Column(db.String(250))
    observacionAvance = db.Column(db.String(250))
    fecha_creacion = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, codigo, cedula, nombres, apellidos, fecha_nacimiento,
                 correo,
                 direccion, ocupacion, telefono, estado, sucursal_id, observacion, observacionAvance,
                 fecha_creacion):
        self.codigo = codigo
        self.cedula = cedula
        self.nombres = nombres
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento
        self.correo = correo
        self.direccion = direccion
        self.ocupacion = ocupacion
        self.telefono = telefono
        self.estado = estado
        self.sucursal_id = sucursal_id
        self.observacion = observacion
        self.observacionAvance = observacionAvance
        self.fecha_creacion = datetime.utcnow()

    def __str__(self):
        return f"id: {self.id}: codigo: {self.codigo} cedula: {self.cedula} nombres: {self.nombres}"

    def getid(self):
        return self.id

    def json(self):
        return {
            "id": self.id,
            "codigo": self.codigo,
            "cedula": self.cedula,
            "nombres": self.nombres,
            "apellidos": self.apellidos,
            "fecha_nacimiento": str(self.fecha_nacimiento),
            "correo": self.correo,
            "direccion": self.direccion,
            "ocupacion": self.ocupacion,
            "telefono": self.telefono,
            "estado": self.estado,
            "sucursal_id": {
                "id": self.sucursal_id,
                "nombre": self.sucursal.nombre,
                "direccion": self.sucursal.direccion,
                "estado": self.sucursal.estado
            },
            "observacion": self.observacion,
            "observacionAvance": self.observacionAvance,
            "fecha_creacion": str(self.fecha_creacion),

        }

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_cedula(cls, cedula):
        return cls.query.filter_by(cedula=cedula).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_correo(cls, correo):
        return cls.query.filter_by(correo=correo).first()

    @classmethod
    def find_by_codigo(cls, codigo):
        return cls.query.filter_by(codigo=codigo).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

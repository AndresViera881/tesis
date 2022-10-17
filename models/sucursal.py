from db import db

class SucursalModel(db.Model):
    __tablename__ = "sucursal"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique=True)
    direccion = db.Column(db.String(150))
    estado = db.Column(db.Boolean, default=True)
    paciente_ = db.relationship('PacienteModel', lazy='dynamic', viewonly=True)
    medico = db.relationship('MedicoModel', lazy='dynamic', viewonly=True)

    def __init__(self, nombre, direccion, estado):
        self.nombre = nombre
        self.direccion = direccion
        self.estado = estado

    def __str__(self):
        return f"id: {self.id}: nombre: {self.nombre} direccion: {self.direccion}"

    def json(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "direccion": self.direccion,
            "estado": self.estado,
            "paciente": [pacientes.json() for pacientes in self.paciente_.all()]
        }

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_nombre(cls, nombre):
        return cls.query.filter_by(nombre=nombre).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

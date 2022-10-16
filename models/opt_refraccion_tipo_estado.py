from db import db


class RefraccionTipoEstadoModel(db.Model):
    __tablename__ = "opt_refraccion_tipo_estado"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)

    refraccionestado = db.relationship('RefraccionEstadoModel', lazy='dynamic', viewonly=True)

    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"id: {self.id}: nombre: {self.nombre}"

    def json(self):
        return {
            "id": self.id,
            "nombre": self.nombre
        }

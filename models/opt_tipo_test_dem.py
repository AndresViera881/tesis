from db import db


class OptTipoTestDemModel(db.Model):
    __tablename__ = "opt_tipo_test_dem"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)

    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"id: {self.id}: nombre: {self.nombre}"

    def json(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
        }

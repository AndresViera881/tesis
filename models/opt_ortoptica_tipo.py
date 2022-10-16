from db import db


class OrtopticaTipoModel(db.Model):
    __tablename__ = "opt_ortoptica_tipo"
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String)

    def __init__(self, tipo):
        self.tipo = tipo

    def __str__(self):
        return f"id: {self.id}: tipo: {self.tipo}"

    def json(self):
        return {
            "id": self.id,
            "tipo": self.tipo,
        }

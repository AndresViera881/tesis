from db import db


class Opt_Diagnostico(db.Model):
    __tablename__ = "opt_diagnostico"

    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(10))
    diagnostico = db.Column(db.String)

    def __init__(self, codigo, diagnostico):
        self.codigo = codigo
        self.diagnostico = diagnostico

    def __str__(self):
        return f"id: {self.id}:codigo: {self.codigo}__nombre: {self.diagnostico}"

    def json(self):
        return {
            "id": self.id,
            "codigo": self.codigo,
            "diagnostico": self.diagnostico
        }


class Opt_Especificaciones(db.Model):
    _tablename__ = "opt_especificaciones"

    id = db.Column(db.Integer, primary_key=True)
    especificacion = db.Column(db.String(150))
    detalle = db.Column(db.String)

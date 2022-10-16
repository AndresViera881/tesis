from db import db


class TransaccionModel(db.Model):
    __tablename__ = "transaccion"
    id = db.Column(db.Integer, primary_key=True)
    transaccion = db.Column(db.String(100), unique=True)
    estado = db.Column(db.Boolean, default=True)

    examen = db.relationship('ExamenModel', lazy='dynamic', viewonly=True)

    def __init__(self, transaccion, estado):
        self.transaccion = transaccion
        self.estado = estado

    def __str__(self):
        return f"id: {self.id}: transaccion: {self.transaccion} estado: {self.estado}"

    def json(self):
        return {
            "id": self.id,
            "transaccion": self.transaccion,
            "estado": self.estado,
            "examen": [examens.json() for examens in self.examen.all()]
        }

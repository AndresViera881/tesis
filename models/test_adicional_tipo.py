from db import db


class TestAdicionalTipoModel(db.Model):
    __tablename__ = "test_adicional_tipo"
    id = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Integer)

    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return f"id: {self.id}: valor: {self.valor}"

    def json(self):
        return {
            "id": self.id,
            "valor": self.valor,
    }

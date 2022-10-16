from db import db


class RefraccionEstadoModel(db.Model):
    __tablename__ = "opt_refraccion_estado"
    id = db.Column(db.Integer, primary_key=True)

    examen_id = db.Column(db.Integer, db.ForeignKey('examen.id'))
    examen = db.relationship('ExamenModel', lazy=True)

    tipo_estado_id = db.Column(db.Integer, db.ForeignKey('opt_refraccion_tipo_estado.id'))
    tipo_estado = db.relationship('RefraccionTipoEstadoModel', lazy=True)

    ojoDerecho = db.Column(db.String)
    ojoIzquierdo = db.Column(db.String)

    def __init__(self, examen_id, tipo_estado_id, ojoDerecho, ojoIzquierdo):
        self.examen_id = examen_id
        self.tipo_estado_id = tipo_estado_id
        self.ojoDerecho = ojoDerecho
        self.ojoIzquierdo = ojoIzquierdo

    def __str__(self):
        return f"id: {self.id}: examen_id: {self.examen_id} tipo_estado_id: {self.tipo_estado_id} " \
               f"ojoDerecho: {self.ojoDerecho} ojoIzquierdo: {self.ojoIzquierdo}"

    def json(self):
        return {
            "id": self.id,
            "examen_id": self.examen_id,
            "tipo_estado_id": self.tipo_estado_id,
            "ojoDerecho": self.ojoDerecho,
            "ojoIzquierdo": self.ojoIzquierdo,
        }

    @classmethod
    def find_by_examen_id(cls, examen_id):
        return cls.query.filter_by(examen_id=examen_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

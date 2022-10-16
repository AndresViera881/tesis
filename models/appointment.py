from datetime import datetime, date

from db import db


class AppointmanetModel(db.Model):
    __tablename__ = "appointments"

    id = db.Column(db.Integer, primary_key=True)

    cliente_id = db.Column(db.Integer, db.ForeignKey("tbl_usuario.id"))
    cliente = db.relationship("UsuarioModel", lazy=True)
    ask_date_apt = db.Column(db.DateTime, default=datetime.utcnow())
    date_appoint = db.Column(db.Date, default=date.today())
    time_appoint = db.Column(db.TIMESTAMP, default=datetime.utcnow())
    reason_appoint = db.Column(db.String())

    def __init__(self, cliente_id, reason_appoint):
        self.cliente_id = cliente_id
        self.reason_appoint = reason_appoint

    def __str__(self):
        return f"pacient_id; {self.pacient_id}__ cliente_id: {self.cliente_id}"

    def json(self):
        return {
            "id": self.id,
            "cliente_id": self.cliente_id,
            "ask_date": str(self.ask_date_apt),
            "date_appoint": str(self.date_appoint),
            "time_appoint": str(self.time_appoint),
            "reason_appoint": self.reason_appoint,
            "clientela": {
                "id": self.cliente_id,
                "public_id": self.cliente.public_id,
                "nombre": self.cliente.nombre,
                "apellidos": self.cliente.apellidos,
                "cedula": self.cliente.cedula,
                "sexo": self.cliente.sexo,
                "direccion": self.cliente.direccion,
                # "fecha_nacimiento": self.cliente_.fecha_nacimiento,
                "correo": self.cliente.direccion,
                "password": self.cliente.password
            },
        }

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

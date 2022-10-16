from datetime import date, time, datetime

from db import db


class AppointmanetModel(db.Model):
    __tablename__ = "appointments"

    id = db.Column(db.Integer, primary_key=True)

    pacient_id = db.Column(db.Integer, db.ForeignKey("paciente.id"))
    pacient_ = db.relationship("PacienteModel", lazy=True)
    admusuario_id = db.Column(db.Integer, db.ForeignKey('admusuario.id'))
    admusuario_ = db.relationship('AdmUsuario', lazy=True)

    ask_date_apt = db.Column(db.DateTime, default=datetime.utcnow())
    date_appoint = db.Column(db.Date)
    time_appoint = db.Column(db.TIMESTAMP)
    reason_appoint = db.Column(db.String())

    def __init__(self, pacient_id, admusuario_id, date_appoint, time_appoint, reason_appoint):
        self.pacient_id = pacient_id
        self.admusuario_id = admusuario_id
        self.date_appoint = date_appoint
        self.time_appoint = time_appoint
        self.reason_appoint = reason_appoint

    def __str__(self):
        return f"pacient_id; {self.pacient_id}"

    def json(self):
        return {
            "id": self.id,
            "ask_date": self.ask_date_apt,
            "date_appoint": self.date_appoint,
            "time_appoint": self.time_appoint,
            "reason_appoint": self.reason_appoint,
            "pacient": {
                "id": self.pacient_.id,
                "codigo": self.pacient_.codigo,
                "cedula": self.pacient_.cedula,
                "nombres": self.pacient_.nombres,
                "apellidos": self.pacient_.apellidos,
                "email": self.pacient_.email,
                "correo": self.pacient_.correo,
                "direccion": self.pacient_.direccion,
                "ocupacion": self.pacient_.ocupacion,
                "telefono": self.pacient_.telefono,
                "estado": self.pacient_.estado,
                "observacion": self.pacient_.observacion,
                "observacionAvance": self.pacient_.observacionAvance,
            },
            "medico": {
                "id": self.admusuario_id,
                "cedula": self.admusuario_.cedula,
                "nombres":self.admusuario_nombres,
                "apellidos": self.admusuario_.apellidos,
                "admrol": {
                    "id": self.admusuario_.admrol_id,
                    "rol": self.admusuario_.admrol.rol,
                    "descripcion": self.admusuario_.admrol.descripcion
                }
            }
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

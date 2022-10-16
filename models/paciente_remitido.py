from db import db


# TABLA PACIENTE_REMITIDO
class pacienteRemitidoModel(db.Model):
    __tablename__ = "paciente_remitido"
    id = db.Column(db.Integer, primary_key=True)
    remitidoDe = db.Column(db.String(200))
    remitidoObservacion = db.Column(db.String(200))

    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id'))
    paciente = db.relationship('PacienteModel', lazy=True)

    def __init__(self, paciente_id, remitidoDe, remitidoObservacion):
        self.paciente_id = paciente_id
        self.remitidoDe = remitidoDe
        self.remitidoObservacion = remitidoObservacion

    def json(self):
        return {
            "id": self.id,
            "paciente_id": self.paciente_id,
            "remitidoDe": self.remitidoDe,
            "remitidoObservacion": self.remitidoObservacion,
            "paciente": [pacientes.json() for pacientes in self.paciente.all()]
        }

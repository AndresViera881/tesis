from datetime import date

from flask_jwt import current_identity

from db import db


class ExamenModel(db.Model):
    __tablename__ = "examen"

    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, default=date.today())

    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id'))
    paciente = db.relationship('PacienteModel', lazy=True)

    medico_id = db.Column(db.Integer, db.ForeignKey('tbl_medicos.id'))
    medico_ = db.relationship('MedicoModel', lazy=True)

    admin_id = db.Column(db.Integer, db.ForeignKey('admin_usuarios.id'))
    admin = db.relationship('AdminUsuario', lazy=True)

    id_transaccion = db.Column(db.Integer, db.ForeignKey('transaccion.id'))
    transaccion = db.relationship('TransaccionModel', lazy=True)

    estado = db.Column(db.Boolean, default=True)

    opt_lentes_contacto = db.relationship('Opt_Lentes_Contacto', lazy='dynamic')
    opt_refraccion_vision = db.relationship('RefraccionVisionModel', lazy='dynamic')

    # @id.setter
    # def id(self, _):
    #     self._id = ExamenModel.CURRENT_ID_VALUE
    #     ExamenModel.CURRENT_ID_VALUE += 1

    def __init__(self, paciente_id, medico_id, id_transaccion, estado):
        self.admin_id = current_identity.getid()
        self.paciente_id = paciente_id
        self.medico_id = medico_id
        self.id_transaccion = id_transaccion
        self.estado = estado

    def __str__(self):
        return f"id: {self.id}: transaccion: {self.transaccion} estado: {self.estado}"

    def getIdExm(self):
        return self.id

    def json(self):
        return {
            "id": self.id,
            "fecha": str(self.fecha),
            "estado": self.estado,
            "medico": {
                "id": self.medico_id,
                "codigo": self.medico_.codigo,
                "cedula": self.medico_.cedula,
                "nombre": self.medico_.nombre,
                "apellidos": self.medico_.apellidos,
                "telefono": self.medico_.sexe,
                "specialidad": {
                    "id": self.medico_.admspecialidad_id,
                    "nombre": self.medico_.admspecialidad.nombre,
                    "descripcion": self.medico_.admspecialidad.descripcion,
                    "estado": self.medico_.admspecialidad.estado
                },
            },
            "paciente": {
                "id": self.paciente_id,
                "codigo": self.paciente.codigo,
                "cedula": self.paciente.cedula,
                "nombres": self.paciente.nombres,
                "apellidos": self.paciente.apellidos,

            },
            "transaccion": {
                "id": self.id_transaccion,
                "transaccion": self.transaccion.transaccion
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

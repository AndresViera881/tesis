from db import db


class RefraccionModel(db.Model):
    __tablename__ = "opt_refraccion"
    id = db.Column(db.Integer, primary_key=True)

    examen_id = db.Column(db.Integer, db.ForeignKey('examen.id'))
    examen = db.relationship('ExamenModel', lazy=True)

    finalOjoDerecho = db.Column(db.String)
    puntajeFinalOjoDerecho = db.Column(db.String)
    finalOjoIzquierdo = db.Column(db.String)
    puntajeFinalOjoIzquierdo = db.Column(db.String)
    finalAdd = db.Column(db.String)
    puntajeFinalAdd = db.Column(db.String)
    titMus = db.Column(db.Float)
    ishihara = db.Column(db.String)
    AmslerOD = db.Column(db.String)
    AmslerOI = db.Column(db.String)
    dp = db.Column(db.String)
    diagnostico = db.Column(db.String)
    diagnostico1 = db.Column(db.String)
    diagnostico2 = db.Column(db.String)
    diagnostico3 = db.Column(db.String)
    tratamiento = db.Column(db.String)

    def __init__(self, examen_id, finalOjoDerecho, puntajeFinalOjoDerecho,
                 finalOjoIzquierdo, puntajeFinalOjoIzquierdo, finalAdd, puntajeFinalAdd, titMus, ishihara,
                 AmslerOD, AmslerOI, dp, diagnostico, diagnostico1, diagnostico2, diagnostico3, tratamiento):
        self.examen_id = examen_id
        self.finalOjoDerecho = finalOjoDerecho
        self.puntajeFinalOjoDerecho = puntajeFinalOjoDerecho
        self.finalOjoIzquierdo = finalOjoIzquierdo
        self.puntajeFinalOjoIzquierdo = puntajeFinalOjoIzquierdo
        self.finalAdd = finalAdd
        self.puntajeFinalAdd = puntajeFinalAdd
        self.titMus = titMus
        self.ishihara = ishihara
        self.AmslerOD = AmslerOD
        self.AmslerOI = AmslerOI
        self.dp = dp
        self.diagnostico = diagnostico
        self.diagnostico1 = diagnostico1
        self.diagnostico2 = diagnostico2
        self.diagnostico3 = diagnostico3
        self.tratamiento = tratamiento

    def __str__(self):
        return f"id: {self.id}: examen_id: {self.examen_id} finalOjoDerecho: {self.finalOjoDerecho} " \
               f"puntajeFinalOjoDerecho: {self.puntajeFinalOjoDerecho} finalOjoIzquierdo: {self.finalOjoIzquierdo} " \
               f"puntajeFinalOjoIzquierdo: {self.puntajeFinalOjoIzquierdo} finalAdd: {self.finalAdd} " \
               f"puntajeFinalAdd: {self.puntajeFinalAdd} titMus: {self.titMus} ishihara: {self.ishihara} " \
               f"AmslerOD: {self.AmslerOD} AmslerOI: {self.AmslerOI} dp: {self.dp} diagnostico: {self.diagnostico} " \
               f"diagnostico1: {self.diagnostico1}  diagnostico2: {self.diagnostico2} diagnostico3: {self.diagnostico3} " \
               f"tratamiento: {self.tratamiento}"

    def json(self):
        return {
            "id": self.id,
            "examen": {
                "id": self.examen_id,
                "id_transaccion": self.examen.id_transaccion,
                "fecha": self.examen.fecha,
                "paciente_id": self.examen.paciente_id,
                "estado": self.examen.estado,
                "medico": {
                    "id": self.examen.medico_id,
                    "codigo": self.examen.medico_.codigo,
                    "cedula": self.examen.medico_.cedula,
                    "nombre": self.examen.medico_.nombre,
                    "apellidos": self.examen.medico_.apellidos,
                    "telefono": self.examen.medico_.sexe,
                    "specialidad": {
                        "id": self.examen.medico_.admspecialidad_id,
                        "nombre": self.examen.medico_.admspecialidad.nombre,
                        "descripcion": self.examen.medico_.admspecialidad.descripcion,
                        "estado": self.examen.medico_.admspecialidad.estado
                    },
                },
            },
            "finalOjoDerecho": self.finalOjoDerecho,
            "puntajeFinalOjoDerecho": self.puntajeFinalOjoDerecho,
            "finalOjoIzquierdo": self.finalOjoIzquierdo,
            "puntajeFinalOjoIzquierdo": self.puntajeFinalOjoIzquierdo,
            "finalAdd": self.finalAdd,
            "puntajeFinalAdd": self.puntajeFinalAdd,
            "titMus": self.titMus,
            "ishihara": self.ishihara,
            "AmslerOD": self.AmslerOD,
            "AmslerOI": self.AmslerOI,
            "dp": self.dp,
            "diagnostico": self.diagnostico,
            "diagnostico1": self.diagnostico1,
            "diagnostico2": self.diagnostico2,
            "diagnostico3": self.diagnostico3,
            "tratamiento": self.tratamiento
        }

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_examen_id(cls, examen_id):
        return cls.query.filter_by(examen_id=examen_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

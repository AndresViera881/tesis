from db import db


class OftalmologiaModel(db.Model):
    __tablename__ = "opt_oftalmologia"
    id = db.Column(db.Integer, primary_key=True)

    examen_id = db.Column(db.Integer, db.ForeignKey('examen.id'))
    examen = db.relationship('ExamenModel', lazy=True)

    OftOjoDerecho = db.Column(db.String)
    imagenOftOjoDerecho = db.Column(db.String)
    OftOjoIzquierdo = db.Column(db.String)
    imagenOftOjoIzquierdo = db.Column(db.String)
    BioOjoDerecho = db.Column(db.String)
    imagenBioOjoDerecho = db.Column(db.String)
    BioOjoIzquierdo = db.Column(db.String)
    imagenBioOjoIzquierdo = db.Column(db.String)
    tratamiento = db.Column(db.String)
    diagnostico = db.Column(db.String)
    diagnostico1 = db.Column(db.String)
    diagnostico2 = db.Column(db.String)
    diagnostico3 = db.Column(db.String)
    vlOjoDerechoSC = db.Column(db.String)
    vlOjoIzquierdoSC = db.Column(db.String)
    vlOjoDerechoCC = db.Column(db.String)
    vlOjoIzquierdoCC = db.Column(db.String)
    consulta = db.Column(db.String)

    def __init__(self, examen_id, OftOjoDerecho, imagenOftOjoDerecho, OftOjoIzquierdo,
                 imagenOftOjoIzquierdo, BioOjoDerecho, imagenBioOjoDerecho, BioOjoIzquierdo,
                 imagenBioOjoIzquierdo, tratamiento, diagnostico, diagnostico1, diagnostico2, diagnostico3,
                 vlOjoDerechoSC, vlOjoIzquierdoSC, vlOjoDerechoCC, vlOjoIzquierdoCC, consulta):
        self.examen_id = examen_id
        self.OftOjoDerecho = OftOjoDerecho
        self.imagenOftOjoDerecho = imagenOftOjoDerecho
        self.OftOjoIzquierdo = OftOjoIzquierdo
        self.imagenOftOjoIzquierdo = imagenOftOjoIzquierdo
        self.BioOjoDerecho = BioOjoDerecho
        self.imagenBioOjoDerecho = imagenBioOjoDerecho
        self.BioOjoIzquierdo = BioOjoIzquierdo
        self.imagenBioOjoIzquierdo = imagenBioOjoIzquierdo
        self.tratamiento = tratamiento
        self.diagnostico = diagnostico
        self.diagnostico1 = diagnostico1
        self.diagnostico2 = diagnostico2
        self.diagnostico3 = diagnostico3
        self.vlOjoDerechoSC = vlOjoDerechoSC
        self.vlOjoIzquierdoSC = vlOjoIzquierdoSC
        self.vlOjoDerechoCC = vlOjoDerechoCC
        self.vlOjoIzquierdoCC = vlOjoIzquierdoCC
        self.consulta = consulta

    def __str__(self):
        return f"id: {self.id}: examen_id: {self.examen_id} OftOjoDerecho: {self.OftOjoDerecho} " \
               f"imagenOftOjoDerecho: {self.imagenOftOjoDerecho} OftOjoIzquierdo: {self.OftOjoIzquierdo} " \
               f"imagenOftOjoIzquierdo: {self.imagenOftOjoIzquierdo} BioOjoDerecho: {self.BioOjoDerecho} " \
               f"imagenBioOjoDerecho: {self.imagenBioOjoDerecho} BioOjoIzquierdo: {self.BioOjoIzquierdo} " \
               f"imagenBioOjoIzquierdo: {self.imagenBioOjoIzquierdo} tratamiento: {self.tratamiento} " \
               f"diagnostico: {self.diagnostico} diagnostico1: {self.diagnostico1} diagnostico2 : {self.diagnostico2} " \
               f"diagnostico3: {self.diagnostico3} vlOjoDerechoSC: {self.vlOjoDerechoSC} vlOjoIzquierdoSC: {self.vlOjoIzquierdoSC} " \
               f"vlOjoDerechoCC: {self.vlOjoDerechoCC} vlOjoIzquierdoCC: {self.vlOjoIzquierdoCC} consulta: {self.consulta}"

    def json(self):
        return {
            "id": self.id,
            "examen": {
                "id": self.examen_id,
                "id_transaccion": self.examen.id_transaccion,
                "fecha": str(self.examen.fecha),
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
            "OftOjoDerecho": self.OftOjoDerecho,
            "imagenOftOjoDerecho": self.imagenOftOjoDerecho,
            "OftOjoIzquierdo": self.OftOjoIzquierdo,
            "imagenOftOjoIzquierdo": self.imagenOftOjoIzquierdo,
            "BioOjoDerecho": self.BioOjoDerecho,
            "imagenBioOjoDerecho": self.imagenBioOjoDerecho,
            "BioOjoIzquierdo": self.BioOjoIzquierdo,
            "imagenBioOjoIzquierdo": self.imagenBioOjoIzquierdo,
            "tratamiento": self.tratamiento,
            "diagnostico": self.diagnostico,
            "diagnostico1": self.diagnostico1,
            "diagnostico2": self.diagnostico2,
            "diagnostico3": self.diagnostico3,
            "vlOjoDerechoSC": self.vlOjoDerechoSC,
            "vlOjoIzquierdoSC": self.vlOjoIzquierdoSC,
            "vlOjoDerechoCC": self.vlOjoDerechoCC,
            "vlOjoIzquierdoCC": self.vlOjoIzquierdoCC,
            "consulta": self.consulta,

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

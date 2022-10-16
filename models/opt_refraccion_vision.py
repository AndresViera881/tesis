from db import db


class RefraccionVisionModel(db.Model):
    __tablename__ = "opt_refraccion_vision"

    id = db.Column(db.Integer, primary_key=True)

    examen_id = db.Column(db.Integer, db.ForeignKey('examen.id'))
    examen = db.relationship('ExamenModel', lazy=True, viewonly=True)

    vlOjoDerechoSC = db.Column(db.String(250))
    vlOjoIzquierdoSC = db.Column(db.String(250))
    vlOjoDerechoCC = db.Column(db.String(250))
    vlOjoIzquierdoCC = db.Column(db.String(250))
    vpOjoDerechoSC = db.Column(db.String(250))
    vpOjoIzquierdoSC = db.Column(db.String(250))
    vpOjoDerechoCC = db.Column(db.String(250))
    vpOjoIzquierdoCC = db.Column(db.String(250))
    rxOjoDerecho = db.Column(db.String(250))
    rxOjoIzquierdo = db.Column(db.String(250))
    qtOjoDerecho = db.Column(db.String(250))
    qtOjoIzquierdo = db.Column(db.String(250))
    atrOjoDerecho = db.Column(db.String(250))
    atrOjoIzquierdo = db.Column(db.String(250))
    estOD = db.Column(db.String(50))
    cylOD = db.Column(db.String(50))
    ejeOD = db.Column(db.String(50))
    addOD = db.Column(db.String(50))
    estOI = db.Column(db.String(50))
    cylOI = db.Column(db.String(50))
    ejeOI = db.Column(db.String(50))
    addOI = db.Column(db.String(50))

    def __init__(self, examen_id, vlOjoDerechoSC, vlOjoIzquierdoSC, vlOjoDerechoCC, vlOjoIzquierdoCC, vpOjoDerechoSC,
                 vpOjoIzquierdoSC,
                 vpOjoDerechoCC, vpOjoIzquierdoCC, rxOjoDerecho, rxOjoIzquierdo, qtOjoDerecho, qtOjoIzquierdo,
                 atrOjoDerecho,
                 atrOjoIzquierdo, estOD, cylOD, ejeOD, addOD, estOI, cylOI, ejeOI, addOI):
        self.examen_id = examen_id
        self.vlOjoDerechoSC = vlOjoDerechoSC
        self.vlOjoIzquierdoSC = vlOjoIzquierdoSC
        self.vlOjoDerechoCC = vlOjoDerechoCC
        self.vlOjoIzquierdoCC = vlOjoIzquierdoCC
        self.vpOjoDerechoSC = vpOjoDerechoSC
        self.vpOjoIzquierdoSC = vpOjoIzquierdoSC
        self.vpOjoDerechoCC = vpOjoDerechoCC
        self.vpOjoIzquierdoCC = vpOjoIzquierdoCC
        self.rxOjoDerecho = rxOjoDerecho
        self.rxOjoIzquierdo = rxOjoIzquierdo
        self.qtOjoDerecho = qtOjoDerecho
        self.qtOjoIzquierdo = qtOjoIzquierdo
        self.atrOjoDerecho = atrOjoDerecho
        self.atrOjoIzquierdo = atrOjoIzquierdo
        self.estOD = estOD
        self.cylOD = cylOD
        self.ejeOD = ejeOD
        self.addOD = addOD
        self.estOI = estOI
        self.cylOI = cylOI
        self.ejeOI = ejeOI
        self.addOI = addOI

    def __str__(self):
        return f"id: {self.id}: examen_id: {self.examen_id} vlOjoDerechoSC: {self.vlOjoDerechoSC} " \
               f"vlOjoIzquierdoSC: {self.vlOjoIzquierdoSC} vlOjoDerechoCC: {self.vlOjoDerechoCC} " \
               f"vlOjoIzquierdoCC: {self.vlOjoDerechoCC} vpOjoDerechoSC: {self.vpOjoDerechoSC} " \
               f"vpOjoIzquierdoSC: {self.vpOjoIzquierdoSC} rxOjoDerecho: {self.rxOjoDerecho} " \
               f"rxOjoIzquierdo: {self.rxOjoIzquierdo} qtOjoDerecho: {self.qtOjoDerecho} " \
               f"qtOjoIzquierdo:{self.qtOjoIzquierdo} atrOjoDerecho: {self.atrOjoDerecho} " \
               f"atrOjoIzquierdo:{self.atrOjoIzquierdo} estOD: {self.estOD} cylOD: {self.cylOD} " \
               f"ejeOD:{self.ejeOD} addOD: {self.addOD} estOI: {self.estOI} cylOI: {self.cylOI} " \
               f"ejeOI: {self.ejeOI} addOI: {self.addOI}"

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
            "vlOjoDerechoSC": self.vlOjoDerechoSC,
            "vlOjoIzquierdoSC": self.vlOjoIzquierdoSC,
            "vlOjoDerechoCC": self.vlOjoDerechoCC,
            "vlOjoIzquierdoCC": self.vlOjoIzquierdoCC,
            "vpOjoDerechoSC": self.vpOjoDerechoSC,
            "vpOjoIzquierdoSC": self.vpOjoIzquierdoSC,
            "qtOjoDerecho": self.qtOjoDerecho,
            "qtOjoIzquierdo": self.qtOjoIzquierdo,
            "atrOjoDerecho": self.atrOjoDerecho,
            "atrOjoIzquierdo": self.atrOjoIzquierdo,
            "estOD": self.estOD,
            "cylOD": self.cylOD,
            "ejeOD": self.ejeOD,
            "addOD": self.addOD,
            "estOI": self.estOI,
            "cylOI": self.cylOI,
            "ejeOI": self.ejeOI,
            "addOI": self.addOI,
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

from db import db


class Opt_Lentes_Contacto(db.Model):
    __tablename__ = "opt_lentes_contacto"
    id = db.Column(db.Integer, primary_key=True)

    examen_id = db.Column(db.Integer, db.ForeignKey('examen.id'))
    examen = db.relationship('ExamenModel', viewonly=True)

    examenExternoOjoDerecho = db.Column(db.String(200))
    examenExternoOjoIzquierdo = db.Column(db.String(200))
    topografiaOjoDerecho = db.Column(db.String)
    topografiaOjoIzquierdo = db.Column(db.String)
    but = db.Column(db.String)
    schirmer = db.Column(db.String)
    curvaFinalOD = db.Column(db.String)
    poderFinalOD = db.Column(db.String)
    diametroFinalOD = db.Column(db.String)
    materialFinalOD = db.Column(db.String)
    disenoFinalOD = db.Column(db.String)
    curvaFinalOI = db.Column(db.String)
    poderFinalOI = db.Column(db.String)
    diametroFinalOI = db.Column(db.String)
    materialFinalOI = db.Column(db.String)
    disenoFinalOI = db.Column(db.String)

    def __init__(self, examen_id, examenExternoOjoDerecho, examenExternoOjoIzquierdo, topografiaOjoDerecho,
                 topografiaOjoIzquierdo,but, schirmer, curvaFinalOD, poderFinalOD, diametroFinalOD,
                 materialFinalOD, disenoFinalOD, curvaFinalOI, poderFinalOI,
                 diametroFinalOI, materialFinalOI, disenoFinalOI):
        self.examen_id = examen_id
        self.examenExternoOjoDerecho = examenExternoOjoDerecho
        self.examenExternoOjoIzquierdo = examenExternoOjoIzquierdo
        self.topografiaOjoDerecho = topografiaOjoDerecho
        self.topografiaOjoIzquierdo = topografiaOjoIzquierdo
        self.but = but
        self.schirmer = schirmer
        self.curvaFinalOD = curvaFinalOD
        self.poderFinalOD = poderFinalOD
        self.diametroFinalOD = diametroFinalOD
        self.materialFinalOD = materialFinalOD
        self.disenoFinalOD = disenoFinalOD
        self.curvaFinalOI = curvaFinalOI
        self.poderFinalOI = poderFinalOI
        self.diametroFinalOI = diametroFinalOI
        self.materialFinalOI = materialFinalOI
        self.disenoFinalOI = disenoFinalOI

    def json(self):
        return {
            "id": self.id,
            "examen": {
                "id": self.examen_id,
                "id_transaccion": self.examen.id_transaccion,
                "fecha": self.examen.fecha,
                "paciente_id": self.examen.paciente_id,
                "estado": self.examen.estado,
                "admusuario_id": self.examen.admusuario_id,
            },
            "examenExternoOjoDerecho": self.examenExternoOjoDerecho,
            "examenExternoOjoIzquierdo": self.examenExternoOjoIzquierdo,
            "topografiaOjoDerecho": self.topografiaOjoDerecho,
            "topografiaOjoIzquierdo": self.topografiaOjoIzquierdo,
            "but": self.but,
            "schirmer": self.schirmer,
            "curvaFinalOD": self.curvaFinalOD,
            "poderFinalOD": self.poderFinalOD,
            "diametroFinalOD": self.diametroFinalOD,
            "materialFinalOD": self.materialFinalOD,
            "disenoFinalOD": self.disenoFinalOD,
            "curvaFinalOI": self.curvaFinalOI,
            "poderFinalOI": self.poderFinalOI,
            "diametroFinalOI": self.diametroFinalOI,
            "materialFinalOI": self.materialFinalOI,
            "disenoFinalOI": self.disenoFinalOI
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

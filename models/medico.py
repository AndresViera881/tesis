from datetime import datetime

from db import db

now = datetime.now()
current_time = now.time()


class MedicoModel(db.Model):
    __tablename__ = "tbl_medicos"

    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(15), unique=True)
    cedula = db.Column(db.String(15), unique=True)
    nombre = db.Column(db.String(100))
    apellidos = db.Column(db.String(100))
    telefono = db.Column(db.String(30))
    sexe = db.Column(db.String(15))

    admspecialidad_id = db.Column(db.Integer, db.ForeignKey('medico_specialidad.id'))
    admspecialidad = db.relationship('MedicoSpecialidadModel')

    sucursal_id = db.Column(db.Integer, db.ForeignKey('sucursal.id'))
    sucursal_ = db.relationship('SucursalModel')

    estado = db.Column(db.Boolean, default=True)

    def __init__(self, codigo, cedula, nombre, apellidos, telefono, sexe, admspecialidad_id, sucursal_id, estado):
        self.codigo = codigo
        self.cedula = cedula
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.sexe = sexe
        self.admspecialidad_id = admspecialidad_id
        self.sucursal_id = sucursal_id
        self.estado = estado

    def __str__(self):
        return f"id: {self.id}, cedula: {self.nombre}, nombre: {self.nombre}, apellidos: {self.apellidos}"

    def json(self):
        return {
            "id": self.id,
            "codigo": self.codigo,
            "cedula": self.cedula,
            "nombre": self.nombre,
            "apellidos": self.apellidos,
            "telefono": self.telefono,
            "sexe": self.sexe,
            "adm_specialidad": {
                "id": self.admspecialidad_id,
                "nombre": self.admspecialidad.nombre,
                "description": self.admspecialidad.descripcion,
                "estado": self.admspecialidad.estado
            },
            "sucursal": {
                "id": self.sucursal_id,
                "nombre": self.sucursal_.nombre,
                "direccion": self.sucursal_.direccion,
                "estado": self.sucursal_.estado
            },

            "estado": self.estado,

        }

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_codigo(cls, codigo):
        return cls.query.filter_by(codigo=codigo).first()

    @classmethod
    def find_by_cedula(cls, cedula):
        return cls.query.filter_by(cedula=cedula).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


class MedicoSpecialidadModel(db.Model):
    __tablename__ = "medico_specialidad"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    descripcion = db.Column(db.String(100))
    estado = db.Column(db.Boolean, default=False)

    medico_ = db.relationship('MedicoModel', lazy='dynamic')

    def __init__(self, nombre, descripion, estado):
        self.nombre = nombre
        self.descripcion = descripion
        self.estado = estado

    def __str__(self):
        return f"id: {self.id}, rol: {self.nombre}"

    def json(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "estado": self.estado,
            "medico": [medicos.json() for medicos in self.medico_.all()]
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


class MedicoHorario(db.Model):
    __tablename__ = "medico_horario"

    id = db.Column(db.Integer, primary_key=True)

    medico_id = db.Column(db.Integer, db.ForeignKey('tbl_medicos.id'))
    medico_ = db.relationship('MedicoModel', lazy=True)

    horario_id = db.Column(db.Integer, db.ForeignKey('tbl_horario.id'))
    horario_ = db.relationship('HorarioModel')

    def __init__(self, medico_id, horario_id):
        self.medico_id = medico_id
        self.horario_id = horario_id

    def __str__(self):
        return f"id: {self.id}, medico: {self.medico_id}, nombre: {self.medico_.nombre}, codigo: {self.medico_.codigo}" \
               f"horario: {self.horario_id}"

    def json(self):
        return {
            "id": self.id,
            "medico": self.medico_id,
            "horario": self.horario_id,
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


class HorarioModel(db.Model):
    __tablename__ = "tbl_horario"

    id = db.Column(db.Integer, primary_key=True)
    dia = db.Column(db.String(200))
    horario_inicio = db.Column(db.DateTime, default=datetime.now())
    horario_fin = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, dia, horario_inicio, horario_fin):
        self.dia = dia
        self.horario_inicio = horario_inicio
        self.horario_fin = horario_fin

    def __str__(self):
        return f"id: {self.id}, medico: {self.dia}, horario_inicio: {self.horario_inicio}, horario_fin: {self.horario_fin}"

    def json(self):
        return {
            "id": self.id,
            "dia": self.dia,
            "horario_inicio": self.horario_inicio,
            "horario_fin": self.horario_fin
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

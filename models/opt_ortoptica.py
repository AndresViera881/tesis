from db import db


class OrtopticaModel(db.Model):
    __tablename__ = "opt_ortoptica"

    id = db.Column(db.Integer, primary_key=True)

    examen_id = db.Column(db.Integer, db.ForeignKey('examen.id'))
    examen = db.relationship('ExamenModel', lazy=True)

    Kappa_od = db.Column(db.String)
    Kappa_oi = db.Column(db.String)
    Hishberg = db.Column(db.String)
    Ducciones_od = db.Column(db.String)
    Ducciones_oi = db.Column(db.String)

    Versiones1_Version1 = db.Column(db.String)
    Versiones2_Version1 = db.Column(db.String)
    Versiones3_Version1 = db.Column(db.String)
    Versiones4_Version1 = db.Column(db.String)
    Versiones5_Version1 = db.Column(db.String)
    Versiones6_Version1 = db.Column(db.String)
    Versiones7_Version2 = db.Column(db.String)
    Versiones8_Version2 = db.Column(db.String)
    Versiones9_Version2 = db.Column(db.String)
    Versiones10_Version2 = db.Column(db.String)
    Versiones11_Version2 = db.Column(db.String)
    Versiones12_Version2 = db.Column(db.String)
    observacion = db.Column(db.String)
    CovertTestVL = db.Column(db.String)
    CovertTestVL40cm = db.Column(db.String)
    PPC_OR = db.Column(db.String)
    PPC_LUZ = db.Column(db.String)
    PPC_LUZ_FR = db.Column(db.String)
    Estereopsis = db.Column(db.String)
    Estereopsis_AC_A = db.Column(db.String)
    Vergencia_Reserva_VL_RFP = db.Column(db.String)
    Vergencia_Reserva_VL_RFN = db.Column(db.String)
    Vergencia_Reserva_VL_Facilidad = db.Column(db.String)

    idVergencia_Falla_VL = db.Column(db.Integer)
    # test_adicional_tipo = db.relationship('TestAdicionalTipoModel', lazy=True)

    Vergencia_Reserva_VP_RFP = db.Column(db.String)
    Vergencia_Reserva_VP_RFN = db.Column(db.String)
    Vergencia_Reserva_VP_Facilidad = db.Column(db.String)

    idVergencia_Falla_VP = db.Column(db.Integer)
    # test_adicional_tipo = db.relationship('TestAdicionalTipoModel', lazy='dynamic')

    ACC_Mem = db.Column(db.Boolean)
    ACC_Nott = db.Column(db.Boolean)
    ACC_OD = db.Column(db.String)
    ACC_OI = db.Column(db.String)
    ACC_ARP = db.Column(db.String)
    ACC_ARN = db.Column(db.String)
    Facilidad_ACC_OD = db.Column(db.String)

    idVergencia_Facilidad_ACC_OD = db.Column(db.Integer)
    # test_adicional_tipo = db.relationship('TestAdicionalTipoModel', lazy=True)

    Facilidad_ACC_OI = db.Column(db.String)

    idVergencia_Facilidad_ACC_OI = db.Column(db.Integer)
    # test_adicional_tipo = db.relationship('TestAdicionalTipoModel', lazy='dynamic')

    Facilidad_ACC_AMBOS = db.Column(db.String)

    idVergencia_Facilidad_ACC_AMBOS = db.Column(db.Integer)
    # test_adicional_tipo = db.relationship('TestAdicionalTipoModel', lazy='dynamic')

    AA_Moda_Subjetivo_OD = db.Column(db.String)
    AA_Moda_Subjetivo_OI = db.Column(db.String)
    AA_Moda_Objetivo_OD = db.Column(db.String)
    AA_Moda_Objetivo_OI = db.Column(db.String)
    Cuadro_Medidas_VL1 = db.Column(db.String)
    Cuadro_Medidas_VL2 = db.Column(db.String)
    Cuadro_Medidas_VL3 = db.Column(db.String)
    Cuadro_Medidas_VL4 = db.Column(db.String)
    Cuadro_Medidas_VL5 = db.Column(db.String)
    Cuadro_Medidas_VL6 = db.Column(db.String)
    Cuadro_Medidas_VL7 = db.Column(db.String)
    Cuadro_Medidas_VL8 = db.Column(db.String)
    Cuadro_Medidas_VL9 = db.Column(db.String)
    Cuadro_Medidas_VP1 = db.Column(db.String)
    Cuadro_Medidas_VP2 = db.Column(db.String)
    Cuadro_Medidas_VP3 = db.Column(db.String)
    Cuadro_Medidas_VP4 = db.Column(db.String)
    Cuadro_Medidas_VP5 = db.Column(db.String)
    Cuadro_Medidas_VP6 = db.Column(db.String)
    Cuadro_Medidas_VP7 = db.Column(db.String)
    Cuadro_Medidas_VP8 = db.Column(db.String)
    Cuadro_Medidas_VP9 = db.Column(db.String)
    TestAdd = db.Column(db.String)
    Oclusion_Mavlow_VP = db.Column(db.String)
    Test_Bielschosky1 = db.Column(db.String)
    Test_Bielschosky2 = db.Column(db.String)

    Test_Adicionales_Base_Externa = db.Column(db.Integer)
    # test_adicional_tipo = db.relationship('TestAdicionalTipoModel', lazy='dynamic')

    Test_Adicionales_Base_Externa_Positivo = db.Column(db.Boolean)
    Test_Adicionales_Base_Externa_Negativo = db.Column(db.Boolean)
    Vl_Luces_Worth = db.Column(db.String)
    Vp_Luces_Worth = db.Column(db.String)
    Bagolini_Objetivo = db.Column(db.String)
    Bagolini_Subjetivo = db.Column(db.String)
    Mom_Test_Dem_H = db.Column(db.String)
    Mom_Test_Dem_V = db.Column(db.String)
    Mom_Test_Dem_R = db.Column(db.String)

    Mom_Test_Dem_Tipo = db.Column(db.Integer, db.ForeignKey('opt_tipo_test_dem.id'))
    opt_tipo_test_dem = db.relationship('OptTipoTestDemModel', lazy=True)

    Mom_Test_Dem_Sumatoria = db.Column(db.String)
    Mom_Test_Dem_Observaciones = db.Column(db.String)
    Mom_Test_Dem_Diagnostico = db.Column(db.String)
    Mom_Test_Dem_Plan = db.Column(db.String)

    def __init__(self, examen_id, Kappa_od, Kappa_oi, Hishberg, Ducciones_od, Ducciones_oi, Versiones1_Version1,
                 Versiones2_Version1, Versiones3_Version1, Versiones4_Version1, Versiones5_Version1,
                 Versiones6_Version1, Versiones7_Version2, Versiones8_Version2, Versiones9_Version2,
                 Versiones10_Version2, Versiones11_Version2, Versiones12_Version2,

                 observacion,
                 CovertTestVL, CovertTestVL40cm, PPC_OR, PPC_LUZ, PPC_LUZ_FR, Estereopsis,
                 Estereopsis_AC_A, Vergencia_Reserva_VL_RFP, Vergencia_Reserva_VL_RFN,
                 Vergencia_Reserva_VL_Facilidad, idVergencia_Falla_VL,

                 Vergencia_Reserva_VP_RFP,
                 Vergencia_Reserva_VP_RFN, Vergencia_Reserva_VP_Facilidad, idVergencia_Falla_VP,
                 ACC_Mem, ACC_Nott, ACC_OD, ACC_OI, ACC_ARP, ACC_ARN, Facilidad_ACC_OD,
                 idVergencia_Facilidad_ACC_OD, Facilidad_ACC_OI, idVergencia_Facilidad_ACC_OI,
                 Facilidad_ACC_AMBOS, idVergencia_Facilidad_ACC_AMBOS,

                 AA_Moda_Subjetivo_OD,
                 AA_Moda_Subjetivo_OI, AA_Moda_Objetivo_OD, AA_Moda_Objetivo_OI, Cuadro_Medidas_VL1,
                 Cuadro_Medidas_VL2, Cuadro_Medidas_VL3, Cuadro_Medidas_VL4, Cuadro_Medidas_VL5,
                 Cuadro_Medidas_VL6, Cuadro_Medidas_VL7, Cuadro_Medidas_VL8, Cuadro_Medidas_VL9,
                 Cuadro_Medidas_VP1, Cuadro_Medidas_VP2, Cuadro_Medidas_VP3, Cuadro_Medidas_VP4,
                 Cuadro_Medidas_VP5, Cuadro_Medidas_VP6, Cuadro_Medidas_VP7, Cuadro_Medidas_VP8,
                 Cuadro_Medidas_VP9,

                 TestAdd, Oclusion_Mavlow_VP, Test_Bielschosky1,
                 Test_Bielschosky2, Test_Adicionales_Base_Externa,
                 Test_Adicionales_Base_Externa_Positivo, Test_Adicionales_Base_Externa_Negativo,
                 Vl_Luces_Worth, Vp_Luces_Worth, Bagolini_Objetivo, Bagolini_Subjetivo,
                 Mom_Test_Dem_H, Mom_Test_Dem_V, Mom_Test_Dem_R, Mom_Test_Dem_Tipo,
                 Mom_Test_Dem_Sumatoria, Mom_Test_Dem_Observaciones, Mom_Test_Dem_Diagnostico, Mom_Test_Dem_Plan):
        self.examen_id = examen_id
        self.Kappa_od = Kappa_od
        self.Kappa_oi = Kappa_oi
        self.Hishberg = Hishberg
        self.Ducciones_od = Ducciones_od
        self.Ducciones_oi = Ducciones_oi
        self.Versiones1_Version1 = Versiones1_Version1
        self.Versiones2_Version1 = Versiones2_Version1
        self.Versiones3_Version1 = Versiones3_Version1
        self.Versiones4_Version1 = Versiones4_Version1
        self.Versiones5_Version1 = Versiones5_Version1
        self.Versiones6_Version1 = Versiones6_Version1
        self.Versiones7_Version2 = Versiones7_Version2
        self.Versiones8_Version2 = Versiones8_Version2
        self.Versiones9_Version2 = Versiones9_Version2
        self.Versiones10_Version2 = Versiones10_Version2
        self.Versiones11_Version2 = Versiones11_Version2
        self.Versiones12_Version2 = Versiones12_Version2

        self.observacion = observacion
        self.CovertTestVL = CovertTestVL
        self.CovertTestVL40cm = CovertTestVL40cm
        self.PPC_OR = PPC_OR
        self.PPC_LUZ = PPC_LUZ
        self.PPC_LUZ_FR = PPC_LUZ_FR
        self.Estereopsis = Estereopsis
        self.Estereopsis_AC_A = Estereopsis_AC_A
        self.Vergencia_Reserva_VL_RFP = Vergencia_Reserva_VL_RFP
        self.Vergencia_Reserva_VL_RFN = Vergencia_Reserva_VL_RFN
        self.Vergencia_Reserva_VL_Facilidad = Vergencia_Reserva_VL_Facilidad
        self.idVergencia_Falla_VL = idVergencia_Falla_VL

        self.Vergencia_Reserva_VP_RFP = Vergencia_Reserva_VP_RFP
        self.Vergencia_Reserva_VP_RFN = Vergencia_Reserva_VP_RFN
        self.Vergencia_Reserva_VP_Facilidad = Vergencia_Reserva_VP_Facilidad
        self.idVergencia_Falla_VP = idVergencia_Falla_VP
        self.ACC_Mem = ACC_Mem
        self.ACC_Nott = ACC_Nott
        self.ACC_OD = ACC_OD
        self.ACC_OI = ACC_OI
        self.ACC_ARP = ACC_ARP
        self.ACC_ARN = ACC_ARN
        self.Facilidad_ACC_OD = Facilidad_ACC_OD
        self.idVergencia_Facilidad_ACC_OD = idVergencia_Facilidad_ACC_OD
        self.Facilidad_ACC_OI = Facilidad_ACC_OI
        self.idVergencia_Facilidad_ACC_OI = idVergencia_Facilidad_ACC_OI
        self.Facilidad_ACC_AMBOS = Facilidad_ACC_AMBOS
        self.idVergencia_Facilidad_ACC_AMBOS = idVergencia_Facilidad_ACC_AMBOS

        self.AA_Moda_Subjetivo_OD = AA_Moda_Subjetivo_OD
        self.AA_Moda_Subjetivo_OI = AA_Moda_Subjetivo_OI
        self.AA_Moda_Objetivo_OD = AA_Moda_Objetivo_OD
        self.AA_Moda_Objetivo_OI = AA_Moda_Objetivo_OI
        self.Cuadro_Medidas_VL1 = Cuadro_Medidas_VL1
        self.Cuadro_Medidas_VL2 = Cuadro_Medidas_VL2
        self.Cuadro_Medidas_VL3 = Cuadro_Medidas_VL3
        self.Cuadro_Medidas_VL4 = Cuadro_Medidas_VL4
        self.Cuadro_Medidas_VL5 = Cuadro_Medidas_VL5
        self.Cuadro_Medidas_VL6 = Cuadro_Medidas_VL6
        self.Cuadro_Medidas_VL7 = Cuadro_Medidas_VL7
        self.Cuadro_Medidas_VL8 = Cuadro_Medidas_VL8
        self.Cuadro_Medidas_VL9 = Cuadro_Medidas_VL9
        self.Cuadro_Medidas_VP1 = Cuadro_Medidas_VP1
        self.Cuadro_Medidas_VP2 = Cuadro_Medidas_VP2
        self.Cuadro_Medidas_VP3 = Cuadro_Medidas_VP3
        self.Cuadro_Medidas_VP4 = Cuadro_Medidas_VP4
        self.Cuadro_Medidas_VP5 = Cuadro_Medidas_VP5
        self.Cuadro_Medidas_VP6 = Cuadro_Medidas_VP6
        self.Cuadro_Medidas_VP7 = Cuadro_Medidas_VP7
        self.Cuadro_Medidas_VP8 = Cuadro_Medidas_VP8
        self.Cuadro_Medidas_VP9 = Cuadro_Medidas_VP9

        self.TestAdd = TestAdd
        self.Oclusion_Mavlow_VP = Oclusion_Mavlow_VP
        self.Test_Bielschosky1 = Test_Bielschosky1
        self.Test_Bielschosky2 = Test_Bielschosky2
        self.Test_Adicionales_Base_Externa = Test_Adicionales_Base_Externa
        self.Test_Adicionales_Base_Externa_Positivo = Test_Adicionales_Base_Externa_Positivo
        self.Test_Adicionales_Base_Externa_Negativo = Test_Adicionales_Base_Externa_Negativo
        self.Vl_Luces_Worth = Vl_Luces_Worth
        self.Vp_Luces_Worth = Vp_Luces_Worth
        self.Bagolini_Objetivo = Bagolini_Objetivo
        self.Bagolini_Subjetivo = Bagolini_Subjetivo
        self.Mom_Test_Dem_H = Mom_Test_Dem_H
        self.Mom_Test_Dem_V = Mom_Test_Dem_V
        self.Mom_Test_Dem_R = Mom_Test_Dem_R
        self.Mom_Test_Dem_Tipo = Mom_Test_Dem_Tipo
        self.Mom_Test_Dem_Sumatoria = Mom_Test_Dem_Sumatoria
        self.Mom_Test_Dem_Observaciones = Mom_Test_Dem_Observaciones
        self.Mom_Test_Dem_Diagnostico = Mom_Test_Dem_Diagnostico
        self.Mom_Test_Dem_Plan = Mom_Test_Dem_Plan

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
            "Kappa_od": self.Kappa_od,
            "Kappa_oi": self.Kappa_oi,
            "Hishberg": self.Hishberg,
            "Ducciones_od": self.Ducciones_od,
            "Ducciones_oi": self.Ducciones_oi,
            "Versiones1_Version1": self.Versiones1_Version1,
            "Versiones2_Version1": self.Versiones2_Version1,
            "Versiones3_Version1": self.Versiones3_Version1,
            "Versiones4_Version1": self.Versiones4_Version1,
            "Versiones5_Version1": self.Versiones5_Version1,
            "Versiones6_Version1": self.Versiones6_Version1,
            "Versiones7_Version2": self.Versiones7_Version2,
            "Versiones8_Version2": self.Versiones8_Version2,
            "Versiones9_Version2": self.Versiones9_Version2,
            "Versiones10_Version2": self.Versiones10_Version2,
            "Versiones11_Version2": self.Versiones11_Version2,
            "Versiones12_Version2": self.Versiones12_Version2,
            "observacion": self.observacion,
            "CovertTestVL": self.CovertTestVL,
            "CovertTestVL40cm": self.CovertTestVL40cm,
            "PPC_OR": self.PPC_OR,
            "PPC_LUZ": self.PPC_LUZ,
            "PPC_LUZ_FR": self.PPC_LUZ_FR,
            "Estereopsis": self.Estereopsis,
            "Estereopsis_AC_A": self.Estereopsis_AC_A,
            "Vergencia_Reserva_VL_RFP": self.Vergencia_Reserva_VL_RFP,
            "Vergencia_Reserva_VL_RFN": self.Vergencia_Reserva_VL_RFN,
            "Vergencia_Reserva_VL_Facilidad": self.Vergencia_Reserva_VL_Facilidad,
            "idVergencia_Falla_VL": self.idVergencia_Falla_VL,
            "Vergencia_Reserva_VP_RFP": self.Vergencia_Reserva_VP_RFP,
            "Vergencia_Reserva_VP_RFN": self.Vergencia_Reserva_VP_RFN,
            "Vergencia_Reserva_VP_Facilidad": self.Vergencia_Reserva_VP_Facilidad,
            "idVergencia_Falla_VP": self.idVergencia_Falla_VP,
            "ACC_Mem": self.ACC_Mem,
            "ACC_Nott": self.ACC_Nott,
            "ACC_OD": self.ACC_OD,
            "ACC_OI": self.ACC_OI,
            "ACC_ARP": self.ACC_ARP,
            "ACC_ARN": self.ACC_ARN,
            "Facilidad_ACC_OD": self.Facilidad_ACC_OD,
            "idVergencia_Facilidad_ACC_OD": self.idVergencia_Facilidad_ACC_OD,
            "Facilidad_ACC_OI": self.Facilidad_ACC_OI,
            "idVergencia_Facilidad_ACC_OI": self.idVergencia_Facilidad_ACC_OI,
            "Facilidad_ACC_AMBOS": self.Facilidad_ACC_AMBOS,
            "idVergencia_Facilidad_ACC_AMBOS": self.idVergencia_Facilidad_ACC_AMBOS,
            "AA_Moda_Subjetivo_OD": self.AA_Moda_Subjetivo_OD,
            "AA_Moda_Subjetivo_OI": self.AA_Moda_Subjetivo_OI,
            "AA_Moda_Objetivo_OD": self.AA_Moda_Objetivo_OD,
            "AA_Moda_Objetivo_OI": self.AA_Moda_Objetivo_OI,
            "Cuadro_Medidas_VL1": self.Cuadro_Medidas_VL1,
            "Cuadro_Medidas_VL2": self.Cuadro_Medidas_VL2,
            "Cuadro_Medidas_VL3": self.Cuadro_Medidas_VL3,
            "Cuadro_Medidas_VL4": self.Cuadro_Medidas_VL4,
            "Cuadro_Medidas_VL5": self.Cuadro_Medidas_VL5,
            "Cuadro_Medidas_VL6": self.Cuadro_Medidas_VL6,
            "Cuadro_Medidas_VL7": self.Cuadro_Medidas_VL7,
            "Cuadro_Medidas_VL8": self.Cuadro_Medidas_VL8,
            "Cuadro_Medidas_VL9": self.Cuadro_Medidas_VL9,
            "Cuadro_Medidas_VP1": self.Cuadro_Medidas_VP1,
            "Cuadro_Medidas_VP2": self.Cuadro_Medidas_VP2,
            "Cuadro_Medidas_VP3": self.Cuadro_Medidas_VP3,
            "Cuadro_Medidas_VP4": self.Cuadro_Medidas_VP4,
            "Cuadro_Medidas_VP5": self.Cuadro_Medidas_VP5,
            "Cuadro_Medidas_VP6": self.Cuadro_Medidas_VP6,
            "Cuadro_Medidas_VP7": self.Cuadro_Medidas_VP7,
            "Cuadro_Medidas_VP8": self.Cuadro_Medidas_VP8,
            "Cuadro_Medidas_VP9": self.Cuadro_Medidas_VP9,
            "TestAdd": self.TestAdd,
            "Oclusion_Mavlow_VP": self.Oclusion_Mavlow_VP,
            "Test_Bielschosky1": self.Test_Bielschosky1,
            "Test_Bielschosky2": self.Test_Bielschosky2,
            "Test_Adicionales_Base_Externa": self.Test_Adicionales_Base_Externa,
            "Test_Adicionales_Base_Externa_Positivo": self.Test_Adicionales_Base_Externa_Positivo,
            "Test_Adicionales_Base_Externa_Negativo": self.Test_Adicionales_Base_Externa_Negativo,
            "Vl_Luces_Worth": self.Vl_Luces_Worth,
            "Vp_Luces_Worth": self.Vp_Luces_Worth,
            "Bagolini_Objetivo": self.Bagolini_Objetivo,
            "Bagolini_Subjetivo": self.Bagolini_Subjetivo,
            "Mom_Test_Dem_H": self.Mom_Test_Dem_H,
            "Mom_Test_Dem_V": self.Mom_Test_Dem_V,
            "Mom_Test_Dem_R": self.Mom_Test_Dem_R,
            "Mom_Test_Dem_Tipo": self.Mom_Test_Dem_Tipo,
            "Mom_Test_Dem_Sumatoria": self.Mom_Test_Dem_Sumatoria,
            "Mom_Test_Dem_Observaciones": self.Mom_Test_Dem_Observaciones,
            "Mom_Test_Dem_Diagnostico": self.Mom_Test_Dem_Diagnostico,
            "Mom_Test_Dem_Plan": self.Mom_Test_Dem_Plan
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

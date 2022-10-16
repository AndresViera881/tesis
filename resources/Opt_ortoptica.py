from datetime import datetime

from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity

from models.examen import ExamenModel
from models.opt_diagnostico import Opt_Diagnostico
from models.opt_ortoptica import OrtopticaModel
from models.opt_ortoptica_tipo import OrtopticaTipoModel
from models.opt_refraccion import RefraccionModel
from models.opt_refraccion_estado import RefraccionEstadoModel
from models.opt_refraccion_tipo_estado import RefraccionTipoEstadoModel
from models.opt_refraccion_vision import RefraccionVisionModel
from models.opt_tipo_test_dem import OptTipoTestDemModel


class OptOrtopeticResource(Resource):
    parse = reqparse.RequestParser()

    # parse.add_argument("paciente_id", type=str, required=True)

    parse.add_argument("medico_id", type=int, help="completez ce champ", required=True)
    parse.add_argument("id_transaccion", type=int, required=True)
    parse.add_argument("estado", type=bool, default=False)

    parse.add_argument("Kappa_od", type=str)
    parse.add_argument("Kappa_oi", type=str)
    parse.add_argument("Hishberg", type=str)
    parse.add_argument("Ducciones_od", type=str)
    parse.add_argument("Ducciones_oi", type=str)
    parse.add_argument("Versiones1_Version1", type=str)
    parse.add_argument("Versiones2_Version1", type=str)
    parse.add_argument("Versiones3_Version1", type=str)
    parse.add_argument("Versiones4_Version1", type=str)
    parse.add_argument("Versiones5_Version1", type=str)
    parse.add_argument("Versiones6_Version1", type=str)
    parse.add_argument("Versiones7_Version2", type=str)
    parse.add_argument("Versiones8_Version2", type=str)
    parse.add_argument("Versiones9_Version2", type=str)
    parse.add_argument("Versiones10_Version2", type=str)
    parse.add_argument("Versiones11_Version2", type=str)
    parse.add_argument('Versiones12_Version2', type=str)  # 1

    parse.add_argument('observacion', type=str)
    parse.add_argument('CovertTestVL', type=str)  # 3
    parse.add_argument('CovertTestVL40cm', type=str)
    parse.add_argument('PPC_OR', type=str)  # 4
    parse.add_argument('PPC_LUZ', type=str)  # 5
    parse.add_argument('PPC_LUZ_FR', type=str)  # 6
    parse.add_argument('Estereopsis', type=str)  # 7
    parse.add_argument('Estereopsis_AC_A', type=str)  # 8
    parse.add_argument('Vergencia_Reserva_VL_RFP', type=str)  # 9
    parse.add_argument('Vergencia_Reserva_VL_RFN', type=str)  # 10
    parse.add_argument('Vergencia_Reserva_VL_Facilidad', type=str)  # 11
    parse.add_argument('idVergencia_Falla_VL', type=int)  # 12

    parse.add_argument('Vergencia_Reserva_VP_RFP', type=str)  # 12
    parse.add_argument('Vergencia_Reserva_VP_RFN', type=str)  # 12
    parse.add_argument('Vergencia_Reserva_VP_Facilidad', type=str)  # 12
    parse.add_argument('idVergencia_Falla_VP', type=int)  # 12

    parse.add_argument('ACC_Mem', type=bool, required=False)  # 12
    parse.add_argument('ACC_Nott', type=bool, required=False)  # 13
    parse.add_argument('ACC_OD', type=str)  # 14
    parse.add_argument('ACC_OI', type=str)
    parse.add_argument('ACC_ARP', type=str)
    parse.add_argument('ACC_ARN', type=str)
    parse.add_argument('Facilidad_ACC_OD', type=str)

    parse.add_argument('idVergencia_Facilidad_ACC_OD', type=int, required=False)
    parse.add_argument('Facilidad_ACC_OI', type=str)
    parse.add_argument('idVergencia_Facilidad_ACC_OI', type=int, required=False)

    parse.add_argument('Facilidad_ACC_AMBOS', type=str)
    parse.add_argument('idVergencia_Facilidad_ACC_AMBOS', type=int, required=False)

    parse.add_argument("AA_Moda_Subjetivo_OD", type=str)
    parse.add_argument("AA_Moda_Subjetivo_OI", type=str)
    parse.add_argument("AA_Moda_Objetivo_OD", type=str)

    parse.add_argument("AA_Moda_Objetivo_OI", type=str)
    parse.add_argument("Cuadro_Medidas_VL1", type=str)
    parse.add_argument("Cuadro_Medidas_VL2", type=str)
    parse.add_argument("Cuadro_Medidas_VL3", type=str)
    parse.add_argument("Cuadro_Medidas_VL4", type=str)
    parse.add_argument("Cuadro_Medidas_VL5", type=str)
    parse.add_argument("Cuadro_Medidas_VL6", type=str)
    parse.add_argument("Cuadro_Medidas_VL7", type=str)
    parse.add_argument("Cuadro_Medidas_VL8", type=str)
    parse.add_argument("Cuadro_Medidas_VL9", type=str)
    parse.add_argument("Cuadro_Medidas_VP1", type=str)
    parse.add_argument("Cuadro_Medidas_VP2", type=str)
    parse.add_argument("Cuadro_Medidas_VP3", type=str)
    parse.add_argument("Cuadro_Medidas_VP4", type=str)
    parse.add_argument("Cuadro_Medidas_VP5", type=str)
    parse.add_argument("Cuadro_Medidas_VP6", type=str)
    parse.add_argument("Cuadro_Medidas_VP7", type=str)
    parse.add_argument("Cuadro_Medidas_VP8", type=str)
    parse.add_argument("Cuadro_Medidas_VP9", type=str)
    parse.add_argument("TestAdd", type=str)
    parse.add_argument("Oclusion_Mavlow_VP", type=str)
    parse.add_argument("Test_Bielschosky1", type=str)
    parse.add_argument("Test_Bielschosky2", type=str)

    parse.add_argument("Test_Adicionales_Base_Externa", type=int, required=False)

    parse.add_argument("Test_Adicionales_Base_Externa_Positivo", type=bool, required=False)
    parse.add_argument("Test_Adicionales_Base_Externa_Negativo", type=bool, required=False)
    parse.add_argument("Vl_Luces_Worth", type=str)
    parse.add_argument("Vp_Luces_Worth", type=str)
    parse.add_argument("Bagolini_Objetivo", type=str)
    parse.add_argument("Bagolini_Subjetivo", type=str)
    parse.add_argument("Mom_Test_Dem_H", type=str)
    parse.add_argument("Mom_Test_Dem_V", type=str)
    parse.add_argument("Mom_Test_Dem_R", type=str)
    parse.add_argument("Mom_Test_Dem_Tipo", type=int)

    # parse.add_argument("opt_tipo_test_dem", type=int, help="completez ce champ")

    parse.add_argument("Mom_Test_Dem_Sumatoria", type=str)
    parse.add_argument("Mom_Test_Dem_Observaciones", type=str)
    parse.add_argument("Mom_Test_Dem_Diagnostico", type=str)
    parse.add_argument("Mom_Test_Dem_Plan", type=str)

    @jwt_required()
    def get(self, id):
        if current_identity.super_admin == True or current_identity.admin_hospital == True:
            ortopticaById = OrtopticaModel.find_by_examen_id(id)
            if ortopticaById:
                return ortopticaById.json()
            return {"message": "Ortoptica not found"}, 404
        else:
            return {"message": "You are not admin"}, 401

    @jwt_required()
    def post(self, paciente_id, transaccion_id):
        data = OptOrtopeticResource.parse.parse_args()
        if current_identity.super_admin == True or current_identity.admin_hospital == True:
            examen = ExamenModel(paciente_id, data['medico_id'], transaccion_id, data['estado'])
            try:
                examen.save_to_db()
            except:
                return {"message": "An error occured inserting the examen."}, 500

            id_examen = examen.getIdExm()

            opt_ortopticamodel = OrtopticaModel(id_examen, data["Kappa_od"], data["Kappa_oi"], data["Hishberg"],
                                                data["Ducciones_od"], data["Ducciones_oi"],
                                                data["Versiones1_Version1"], data["Versiones2_Version1"],
                                                data["Versiones3_Version1"], data["Versiones4_Version1"],
                                                data["Versiones5_Version1"], data["Versiones6_Version1"],
                                                data["Versiones7_Version2"], data["Versiones8_Version2"],
                                                data["Versiones9_Version2"], data["Versiones10_Version2"],
                                                data["Versiones11_Version2"], data["Versiones12_Version2"],
                                                data["observacion"], data["CovertTestVL"], data["CovertTestVL40cm"],
                                                data["PPC_OR"], data["PPC_LUZ"], data["PPC_LUZ_FR"],
                                                data["Estereopsis"],
                                                data["Estereopsis_AC_A"], data["Vergencia_Reserva_VL_RFP"],
                                                data["Vergencia_Reserva_VL_RFN"],
                                                data["Vergencia_Reserva_VL_Facilidad"], data["idVergencia_Falla_VL"],
                                                data["Vergencia_Reserva_VP_RFP"],
                                                data["Vergencia_Reserva_VP_RFN"],
                                                data["Vergencia_Reserva_VP_Facilidad"], data["idVergencia_Falla_VP"],
                                                data["ACC_Mem"], data["ACC_Nott"], data["ACC_OD"],
                                                data["ACC_OI"], data["ACC_ARP"], data["ACC_ARN"],
                                                data["Facilidad_ACC_OD"], data["idVergencia_Facilidad_ACC_OD"],
                                                data["Facilidad_ACC_OI"],
                                                data["idVergencia_Facilidad_ACC_OI"], data["Facilidad_ACC_AMBOS"],
                                                data["idVergencia_Facilidad_ACC_AMBOS"],
                                                data["AA_Moda_Subjetivo_OD"], data["AA_Moda_Subjetivo_OI"],
                                                data["AA_Moda_Objetivo_OD"],
                                                data["AA_Moda_Objetivo_OI"], data["Cuadro_Medidas_VL1"],
                                                data["Cuadro_Medidas_VL2"],
                                                data["Cuadro_Medidas_VL3"], data["Cuadro_Medidas_VL4"],
                                                data["Cuadro_Medidas_VL5"],
                                                data["Cuadro_Medidas_VL6"], data["Cuadro_Medidas_VL7"],
                                                data["Cuadro_Medidas_VL8"],
                                                data["Cuadro_Medidas_VL9"], data["Cuadro_Medidas_VP1"],
                                                data["Cuadro_Medidas_VP2"],
                                                data["Cuadro_Medidas_VP3"], data["Cuadro_Medidas_VP4"],
                                                data["Cuadro_Medidas_VP5"],
                                                data["Cuadro_Medidas_VP6"], data["Cuadro_Medidas_VP7"],
                                                data["Cuadro_Medidas_VP8"],
                                                data["Cuadro_Medidas_VP9"], data["TestAdd"],
                                                data["Oclusion_Mavlow_VP"],
                                                data["Test_Bielschosky1"], data["Test_Bielschosky2"],
                                                data["Test_Adicionales_Base_Externa"],
                                                data["Test_Adicionales_Base_Externa_Positivo"],
                                                data["Test_Adicionales_Base_Externa_Negativo"],
                                                data["Vl_Luces_Worth"],
                                                data["Vp_Luces_Worth"], data["Bagolini_Objetivo"],
                                                data["Bagolini_Subjetivo"],
                                                data["Mom_Test_Dem_H"], data["Mom_Test_Dem_V"],
                                                data["Mom_Test_Dem_R"],
                                                data["Mom_Test_Dem_Tipo"], data["Mom_Test_Dem_Sumatoria"],
                                                data["Mom_Test_Dem_Observaciones"],
                                                data["Mom_Test_Dem_Diagnostico"], data["Mom_Test_Dem_Plan"])

            try:
                opt_ortopticamodel.save_to_db()
            except:
                return {"message": "An error occured inserting the ortoptica examen."}, 500
            return {"message": " Ortoptica is created success"}, 201
        else:
            return {"message": "You don't have authorisation"}, 401


class OptOrtopticaPutRessource(Resource):
    @jwt_required()
    def put(self, id):
        if current_identity.super_admin == True or current_identity.admin_hospital == True:

            ortoptica = OrtopticaModel.find_by_examen_id(id)
            data = OptOrtopeticResource.parse.parse_args()

            if ortoptica:
                ortoptica.Kappa_od = data["Kappa_od"]
                ortoptica.Kappa_oi = data["Kappa_oi"]
                ortoptica.Hishberg = data["Hishberg"]
                ortoptica.Ducciones_od = data["Ducciones_od"]
                ortoptica.Ducciones_oi = data["Ducciones_oi"]
                ortoptica.Versiones1_Version1 = data["Versiones1_Version1"]
                ortoptica.Versiones2_Version1 = data["Versiones2_Version1"]
                ortoptica.Versiones3_Version1 = data["Versiones3_Version1"]
                ortoptica.Versiones4_Version1 = data["Versiones4_Version1"]
                ortoptica.Versiones5_Version1 = data["Versiones5_Version1"]
                ortoptica.Versiones6_Version1 = data["Versiones6_Version1"]
                ortoptica.Versiones7_Version2 = data["Versiones7_Version2"]
                ortoptica.Versiones8_Version2 = data["Versiones8_Version2"]
                ortoptica.Versiones9_Version2 = data["Versiones9_Version2"]
                ortoptica.Versiones10_Version2 = data["Versiones10_Version2"]
                ortoptica.Versiones11_Version2 = data["Versiones11_Version2"]
                ortoptica.Versiones12_Version2 = data["Versiones12_Version2"]
                ortoptica.observacion = data["observacion"]
                ortoptica.CovertTestVL = data["CovertTestVL"]
                ortoptica.CovertTestVL40cm = data["CovertTestVL40cm"]
                ortoptica.PPC_OR = data["PPC_OR"]
                ortoptica.PPC_LUZ = data["PPC_LUZ"]
                ortoptica.PPC_LUZ_FR = data["PPC_LUZ_FR"]
                ortoptica.Estereopsis = data["Estereopsis"]
                ortoptica.Estereopsis_AC_A = data["Estereopsis_AC_A"]
                ortoptica.Vergencia_Reserva_VL_RFP = data["Vergencia_Reserva_VL_RFP"]
                ortoptica.Vergencia_Reserva_VL_RFN = data["Vergencia_Reserva_VL_RFN"]
                ortoptica.Vergencia_Reserva_VL_Facilidad = data["Vergencia_Reserva_VL_Facilidad"]
                ortoptica.idVergencia_Falla_VL = data["idVergencia_Falla_VL"]
                ortoptica.Vergencia_Reserva_VP_RFP = data["Vergencia_Reserva_VP_RFP"]
                ortoptica.Vergencia_Reserva_VP_RFN = data["Vergencia_Reserva_VP_RFN"]
                ortoptica.Vergencia_Reserva_VP_Facilidad = data["Vergencia_Reserva_VP_Facilidad"]
                ortoptica.idVergencia_Falla_VP = data["idVergencia_Falla_VP"]
                ortoptica.ACC_Mem = data["ACC_Mem"]
                ortoptica.ACC_Nott = data["ACC_Nott"]
                ortoptica.ACC_OD = data["ACC_OD"]
                ortoptica.ACC_OI = data["ACC_OI"]
                ortoptica.ACC_ARP = data["ACC_ARP"]
                ortoptica.ACC_ARN = data["ACC_ARN"]
                ortoptica.Facilidad_ACC_OD = data["Facilidad_ACC_OD"]
                ortoptica.idVergencia_Facilidad_ACC_OD = data["idVergencia_Facilidad_ACC_OD"]
                ortoptica.Facilidad_ACC_OI = data["Facilidad_ACC_OI"]
                ortoptica.idVergencia_Facilidad_ACC_OI = data["idVergencia_Facilidad_ACC_OI"]
                ortoptica.Facilidad_ACC_AMBOS = data["Facilidad_ACC_AMBOS"]
                ortoptica.idVergencia_Facilidad_ACC_AMBOS = data["idVergencia_Facilidad_ACC_AMBOS"]
                ortoptica.AA_Moda_Subjetivo_OD = data["AA_Moda_Subjetivo_OD"]
                ortoptica.AA_Moda_Subjetivo_OI = data["AA_Moda_Subjetivo_OI"]
                ortoptica.AA_Moda_Objetivo_OD = data["AA_Moda_Objetivo_OD"]
                ortoptica.AA_Moda_Objetivo_OI = data["AA_Moda_Objetivo_OI"]
                ortoptica.Cuadro_Medidas_VL1 = data["Cuadro_Medidas_VL1"]
                ortoptica.Cuadro_Medidas_VL2 = data["Cuadro_Medidas_VL2"]
                ortoptica.Cuadro_Medidas_VL3 = data["Cuadro_Medidas_VL3"]
                ortoptica.Cuadro_Medidas_VL4 = data["Cuadro_Medidas_VL4"]
                ortoptica.Cuadro_Medidas_VL5 = data["Cuadro_Medidas_VL5"]
                ortoptica.Cuadro_Medidas_VL6 = data["Cuadro_Medidas_VL6"]
                ortoptica.Cuadro_Medidas_VL7 = data["Cuadro_Medidas_VL7"]
                ortoptica.Cuadro_Medidas_VL8 = data["Cuadro_Medidas_VL8"]
                ortoptica.Cuadro_Medidas_VL9 = data["Cuadro_Medidas_VL9"]
                ortoptica.Cuadro_Medidas_VP1 = data["Cuadro_Medidas_VP1"]
                ortoptica.Cuadro_Medidas_VP2 = data["Cuadro_Medidas_VP2"]
                ortoptica.Cuadro_Medidas_VP3 = data["Cuadro_Medidas_VP3"]
                ortoptica.Cuadro_Medidas_VP4 = data["Cuadro_Medidas_VP4"]
                ortoptica.Cuadro_Medidas_VP5 = data["Cuadro_Medidas_VP5"]
                ortoptica.Cuadro_Medidas_VP6 = data["Cuadro_Medidas_VP6"]
                ortoptica.Cuadro_Medidas_VP7 = data["Cuadro_Medidas_VP7"]
                ortoptica.Cuadro_Medidas_VP8 = data["Cuadro_Medidas_VP8"]
                ortoptica.Cuadro_Medidas_VP9 = data["Cuadro_Medidas_VP9"]
                ortoptica.TestAdd = data["TestAdd"]
                ortoptica.Oclusion_Mavlow_VP = data["Oclusion_Mavlow_VP"]
                ortoptica.Test_Bielschosky1 = data["Test_Bielschosky1"]
                ortoptica.Test_Bielschosky2 = data["Test_Bielschosky2"]
                ortoptica.Test_Adicionales_Base_Externa = data["Test_Adicionales_Base_Externa"]
                ortoptica.Test_Adicionales_Base_Externa_Positivo = data["Test_Adicionales_Base_Externa_Positivo"]
                ortoptica.Test_Adicionales_Base_Externa_Negativo = data["Test_Adicionales_Base_Externa_Negativo"]
                ortoptica.Vl_Luces_Worth = data["Vl_Luces_Worth"]
                ortoptica.Vp_Luces_Worth = data["Vp_Luces_Worth"]
                ortoptica.Bagolini_Objetivo = data["Bagolini_Objetivo"]
                ortoptica.Bagolini_Subjetivo = data["Bagolini_Subjetivo"]
                ortoptica.Mom_Test_Dem_H = data["Mom_Test_Dem_H"]
                ortoptica.Mom_Test_Dem_V = data["Mom_Test_Dem_V"]
                ortoptica.Mom_Test_Dem_R = data["Mom_Test_Dem_R"]
                ortoptica.Mom_Test_Dem_Tipo = data["Mom_Test_Dem_Tipo"]
                ortoptica.Mom_Test_Dem_Sumatoria = data["Mom_Test_Dem_Sumatoria"]
                ortoptica.Mom_Test_Dem_Observaciones = data["Mom_Test_Dem_Observaciones"]
                ortoptica.Mom_Test_Dem_Diagnostico = data["Mom_Test_Dem_Diagnostico"]
                ortoptica.Mom_Test_Dem_Plan = data["Mom_Test_Dem_Plan"]
                print('LLego2')
            else:
                ortoptica = OrtopticaModel(id, **data)

            try:
                ortoptica.save_to_db()
            except:
                return {"message": "An error occured update the Examen"}

            return ortoptica.json()
        else:
            return {"message": "You don't have authorisation"}, 401


class OrtopticaTipoRessource(Resource):
    @jwt_required()
    def get(self):
        if current_identity.super_admin == True or current_identity.admin_hospital == True:
            ortopticaTipo = OrtopticaTipoModel.query.all()
            return {"tipo": list(map(lambda x: x.json(), ortopticaTipo))}
        else:
            return {"message": "You don't have authorization"}, 401


class OrtopticaTipoTestDemRessource(Resource):
    @jwt_required()
    def get(self):
        if current_identity.super_admin == True or current_identity.admin_hospital == True:
            ortopticaTipoTestDem = OptTipoTestDemModel.query.all()
            return {"tipoTestDem": list(map(lambda x: x.json(), ortopticaTipoTestDem))}
        else:
            return {"message": "You don't have authorization"}, 401

"""empty message

Revision ID: f2ed2019b5a5
Revises: 
Create Date: 2021-09-13 20:31:42.668284

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f2ed2019b5a5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin_usuarios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cedula', sa.String(length=13), nullable=True),
    sa.Column('nombres', sa.String(length=200), nullable=True),
    sa.Column('apellidos', sa.String(length=200), nullable=True),
    sa.Column('correo', sa.String(length=100), nullable=True),
    sa.Column('password', sa.String(length=200), nullable=True),
    sa.Column('direccion', sa.String(length=250), nullable=True),
    sa.Column('telefono', sa.String(length=20), nullable=True),
    sa.Column('sexe', sa.String(length=15), nullable=True),
    sa.Column('admin_clientela', sa.Boolean(), nullable=True),
    sa.Column('admin_hospital', sa.Boolean(), nullable=True),
    sa.Column('super_admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cedula'),
    sa.UniqueConstraint('correo')
    )
    op.create_table('medico_specialidad',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=True),
    sa.Column('descripcion', sa.String(length=100), nullable=True),
    sa.Column('estado', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('opt__especificaciones',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('especificacion', sa.String(length=150), nullable=True),
    sa.Column('detalle', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('opt_diagnostico',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('codigo', sa.String(length=10), nullable=True),
    sa.Column('diagnostico', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('opt_ortoptica_tipo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tipo', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('opt_refraccion_tipo_estado',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('opt_tipo_test_dem',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sucursal',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=True),
    sa.Column('direccion', sa.String(length=150), nullable=True),
    sa.Column('estado', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nombre')
    )
    op.create_table('tbl_horario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dia', sa.String(length=200), nullable=True),
    sa.Column('horario_inicio', sa.DateTime(), nullable=True),
    sa.Column('horario_fin', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tbl_usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('public_id', sa.String(length=50), nullable=True),
    sa.Column('nombre', sa.String(length=50), nullable=True),
    sa.Column('apellidos', sa.String(length=50), nullable=True),
    sa.Column('cedula', sa.String(length=100), nullable=False),
    sa.Column('sexo', sa.String(length=10), nullable=False),
    sa.Column('direccion', sa.String(length=100), nullable=False),
    sa.Column('fecha_nacimiento', sa.Date(), nullable=True),
    sa.Column('correo', sa.String(length=200), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('verificacion_email', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('correo'),
    sa.UniqueConstraint('public_id')
    )
    op.create_table('test_adicional_tipo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('valor', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('transaccion',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('transaccion', sa.String(length=100), nullable=True),
    sa.Column('estado', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('transaccion')
    )
    op.create_table('appointments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cliente_id', sa.Integer(), nullable=True),
    sa.Column('ask_date_apt', sa.DateTime(), nullable=True),
    sa.Column('date_appoint', sa.Date(), nullable=True),
    sa.Column('time_appoint', sa.TIMESTAMP(), nullable=True),
    sa.Column('reason_appoint', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['cliente_id'], ['tbl_usuario.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('paciente',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('codigo', sa.String(length=100), nullable=True),
    sa.Column('cedula', sa.String(length=13), nullable=True),
    sa.Column('nombres', sa.String(length=250), nullable=True),
    sa.Column('apellidos', sa.String(length=250), nullable=True),
    sa.Column('fecha_nacimiento', sa.Date(), nullable=True),
    sa.Column('correo', sa.String(length=150), nullable=True),
    sa.Column('direccion', sa.String(length=250), nullable=True),
    sa.Column('ocupacion', sa.String(length=250), nullable=True),
    sa.Column('telefono', sa.String(length=10), nullable=True),
    sa.Column('estado', sa.Boolean(), nullable=True),
    sa.Column('sucursal_id', sa.Integer(), nullable=True),
    sa.Column('observacion', sa.String(length=250), nullable=True),
    sa.Column('observacionAvance', sa.String(length=250), nullable=True),
    sa.Column('fecha_creacion', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['sucursal_id'], ['sucursal.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cedula'),
    sa.UniqueConstraint('codigo'),
    sa.UniqueConstraint('correo')
    )
    op.create_table('tbl_medicos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('codigo', sa.String(length=15), nullable=True),
    sa.Column('cedula', sa.String(length=15), nullable=True),
    sa.Column('nombre', sa.String(length=100), nullable=True),
    sa.Column('apellidos', sa.String(length=100), nullable=True),
    sa.Column('telefono', sa.String(length=30), nullable=True),
    sa.Column('sexe', sa.String(length=15), nullable=True),
    sa.Column('admspecialidad_id', sa.Integer(), nullable=True),
    sa.Column('sucursal_id', sa.Integer(), nullable=True),
    sa.Column('estado', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['admspecialidad_id'], ['medico_specialidad.id'], ),
    sa.ForeignKeyConstraint(['sucursal_id'], ['sucursal.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cedula'),
    sa.UniqueConstraint('codigo')
    )
    op.create_table('examen',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fecha', sa.Date(), nullable=True),
    sa.Column('paciente_id', sa.Integer(), nullable=True),
    sa.Column('medico_id', sa.Integer(), nullable=True),
    sa.Column('admin_id', sa.Integer(), nullable=True),
    sa.Column('id_transaccion', sa.Integer(), nullable=True),
    sa.Column('estado', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['admin_id'], ['admin_usuarios.id'], ),
    sa.ForeignKeyConstraint(['id_transaccion'], ['transaccion.id'], ),
    sa.ForeignKeyConstraint(['medico_id'], ['tbl_medicos.id'], ),
    sa.ForeignKeyConstraint(['paciente_id'], ['paciente.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('medico_horario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('medico_id', sa.Integer(), nullable=True),
    sa.Column('horario_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['horario_id'], ['tbl_horario.id'], ),
    sa.ForeignKeyConstraint(['medico_id'], ['tbl_medicos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('paciente_remitido',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('remitidoDe', sa.String(length=200), nullable=True),
    sa.Column('remitidoObservacion', sa.String(length=200), nullable=True),
    sa.Column('paciente_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['paciente_id'], ['paciente.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tbl_citas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fecha', sa.Date(), nullable=True),
    sa.Column('hora', sa.TIMESTAMP(), nullable=True),
    sa.Column('estado', sa.Boolean(), nullable=True),
    sa.Column('cliente_id', sa.Integer(), nullable=True),
    sa.Column('medico_id', sa.Integer(), nullable=True),
    sa.Column('horario_id', sa.Integer(), nullable=True),
    sa.Column('admin_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['admin_id'], ['admin_usuarios.id'], ),
    sa.ForeignKeyConstraint(['cliente_id'], ['tbl_usuario.id'], ),
    sa.ForeignKeyConstraint(['horario_id'], ['tbl_horario.id'], ),
    sa.ForeignKeyConstraint(['medico_id'], ['tbl_medicos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('opt_lentes_contacto',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('examen_id', sa.Integer(), nullable=True),
    sa.Column('examenExternoOjoDerecho', sa.String(length=200), nullable=True),
    sa.Column('examenExternoOjoIzquierdo', sa.String(length=200), nullable=True),
    sa.Column('topografiaOjoDerecho', sa.String(), nullable=True),
    sa.Column('topografiaOjoIzquierdo', sa.String(), nullable=True),
    sa.Column('but', sa.String(), nullable=True),
    sa.Column('schirmer', sa.String(), nullable=True),
    sa.Column('curvaFinalOD', sa.String(), nullable=True),
    sa.Column('poderFinalOD', sa.String(), nullable=True),
    sa.Column('diametroFinalOD', sa.String(), nullable=True),
    sa.Column('materialFinalOD', sa.String(), nullable=True),
    sa.Column('disenoFinalOD', sa.String(), nullable=True),
    sa.Column('curvaFinalOI', sa.String(), nullable=True),
    sa.Column('poderFinalOI', sa.String(), nullable=True),
    sa.Column('diametroFinalOI', sa.String(), nullable=True),
    sa.Column('materialFinalOI', sa.String(), nullable=True),
    sa.Column('disenoFinalOI', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['examen_id'], ['examen.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('opt_oftalmologia',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('examen_id', sa.Integer(), nullable=True),
    sa.Column('OftOjoDerecho', sa.String(), nullable=True),
    sa.Column('imagenOftOjoDerecho', sa.String(), nullable=True),
    sa.Column('OftOjoIzquierdo', sa.String(), nullable=True),
    sa.Column('imagenOftOjoIzquierdo', sa.String(), nullable=True),
    sa.Column('BioOjoDerecho', sa.String(), nullable=True),
    sa.Column('imagenBioOjoDerecho', sa.String(), nullable=True),
    sa.Column('BioOjoIzquierdo', sa.String(), nullable=True),
    sa.Column('imagenBioOjoIzquierdo', sa.String(), nullable=True),
    sa.Column('tratamiento', sa.String(), nullable=True),
    sa.Column('diagnostico', sa.String(), nullable=True),
    sa.Column('diagnostico1', sa.String(), nullable=True),
    sa.Column('diagnostico2', sa.String(), nullable=True),
    sa.Column('diagnostico3', sa.String(), nullable=True),
    sa.Column('vlOjoDerechoSC', sa.String(), nullable=True),
    sa.Column('vlOjoIzquierdoSC', sa.String(), nullable=True),
    sa.Column('vlOjoDerechoCC', sa.String(), nullable=True),
    sa.Column('vlOjoIzquierdoCC', sa.String(), nullable=True),
    sa.Column('consulta', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['examen_id'], ['examen.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('opt_ortoptica',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('examen_id', sa.Integer(), nullable=True),
    sa.Column('Kappa_od', sa.String(), nullable=True),
    sa.Column('Kappa_oi', sa.String(), nullable=True),
    sa.Column('Hishberg', sa.String(), nullable=True),
    sa.Column('Ducciones_od', sa.String(), nullable=True),
    sa.Column('Ducciones_oi', sa.String(), nullable=True),
    sa.Column('Versiones1_Version1', sa.String(), nullable=True),
    sa.Column('Versiones2_Version1', sa.String(), nullable=True),
    sa.Column('Versiones3_Version1', sa.String(), nullable=True),
    sa.Column('Versiones4_Version1', sa.String(), nullable=True),
    sa.Column('Versiones5_Version1', sa.String(), nullable=True),
    sa.Column('Versiones6_Version1', sa.String(), nullable=True),
    sa.Column('Versiones7_Version2', sa.String(), nullable=True),
    sa.Column('Versiones8_Version2', sa.String(), nullable=True),
    sa.Column('Versiones9_Version2', sa.String(), nullable=True),
    sa.Column('Versiones10_Version2', sa.String(), nullable=True),
    sa.Column('Versiones11_Version2', sa.String(), nullable=True),
    sa.Column('Versiones12_Version2', sa.String(), nullable=True),
    sa.Column('observacion', sa.String(), nullable=True),
    sa.Column('CovertTestVL', sa.String(), nullable=True),
    sa.Column('PPC_OR', sa.String(), nullable=True),
    sa.Column('PPC_LUZ', sa.String(), nullable=True),
    sa.Column('PPC_LUZ_FR', sa.String(), nullable=True),
    sa.Column('Estereopsis', sa.String(), nullable=True),
    sa.Column('Estereopsis_AC_A', sa.String(), nullable=True),
    sa.Column('Vergencia_Reserva_VL_RFP', sa.String(), nullable=True),
    sa.Column('Vergencia_Reserva_VL_RFN', sa.String(), nullable=True),
    sa.Column('Vergencia_Reserva_VL_Facilidad', sa.String(), nullable=True),
    sa.Column('idVergencia_Falla_VL', sa.Integer(), nullable=True),
    sa.Column('Vergencia_Reserva_VP_RFP', sa.String(), nullable=True),
    sa.Column('Vergencia_Reserva_VP_RFN', sa.String(), nullable=True),
    sa.Column('Vergencia_Reserva_VP_Facilidad', sa.String(), nullable=True),
    sa.Column('idVergencia_Falla_VP', sa.Integer(), nullable=True),
    sa.Column('ACC_Mem', sa.Boolean(), nullable=True),
    sa.Column('ACC_Nott', sa.Boolean(), nullable=True),
    sa.Column('ACC_OD', sa.String(), nullable=True),
    sa.Column('ACC_OI', sa.String(), nullable=True),
    sa.Column('ACC_ARP', sa.String(), nullable=True),
    sa.Column('ACC_ARN', sa.String(), nullable=True),
    sa.Column('Facilidad_ACC_OD', sa.String(), nullable=True),
    sa.Column('idVergencia_Facilidad_ACC_OD', sa.Integer(), nullable=True),
    sa.Column('Facilidad_ACC_OI', sa.String(), nullable=True),
    sa.Column('idVergencia_Facilidad_ACC_OI', sa.Integer(), nullable=True),
    sa.Column('Facilidad_ACC_AMBOS', sa.String(), nullable=True),
    sa.Column('idVergencia_Facilidad_ACC_AMBOS', sa.Integer(), nullable=True),
    sa.Column('AA_Moda_Subjetivo_OD', sa.String(), nullable=True),
    sa.Column('AA_Moda_Subjetivo_OI', sa.String(), nullable=True),
    sa.Column('AA_Moda_Objetivo_OD', sa.String(), nullable=True),
    sa.Column('AA_Moda_Objetivo_OI', sa.String(), nullable=True),
    sa.Column('Cuadro_Medidas_VL1', sa.String(), nullable=True),
    sa.Column('Cuadro_Medidas_VL2', sa.String(), nullable=True),
    sa.Column('Cuadro_Medidas_VL3', sa.String(), nullable=True),
    sa.Column('Cuadro_Medidas_VL4', sa.String(), nullable=True),
    sa.Column('Cuadro_Medidas_VL5', sa.String(), nullable=True),
    sa.Column('Cuadro_Medidas_VL6', sa.String(), nullable=True),
    sa.Column('Cuadro_Medidas_VL7', sa.String(), nullable=True),
    sa.Column('Cuadro_Medidas_VL8', sa.String(), nullable=True),
    sa.Column('Cuadro_Medidas_VL9', sa.String(), nullable=True),
    sa.Column('Cuadro_Medidas_VP1', sa.String(), nullable=True),
    sa.Column('Cuadro_Medidas_VP2', sa.String(), nullable=True),
    sa.Column('Cuadro_Medidas_VP3', sa.String(), nullable=True),
    sa.Column('Cuadro_Medidas_VP4', sa.String(), nullable=True),
    sa.Column('Cuadro_Medidas_VP5', sa.String(), nullable=True),
    sa.Column('Cuadro_Medidas_VP6', sa.String(), nullable=True),
    sa.Column('Cuadro_Medidas_VP7', sa.String(), nullable=True),
    sa.Column('Cuadro_Medidas_VP8', sa.String(), nullable=True),
    sa.Column('Cuadro_Medidas_VP9', sa.String(), nullable=True),
    sa.Column('TestAdd', sa.String(), nullable=True),
    sa.Column('Oclusion_Mavlow_VP', sa.String(), nullable=True),
    sa.Column('Test_Bielschosky1', sa.String(), nullable=True),
    sa.Column('Test_Bielschosky2', sa.String(), nullable=True),
    sa.Column('Test_Adicionales_Base_Externa', sa.Integer(), nullable=True),
    sa.Column('Test_Adicionales_Base_Externa_Positivo', sa.Boolean(), nullable=True),
    sa.Column('Test_Adicionales_Base_Externa_Negativo', sa.Boolean(), nullable=True),
    sa.Column('Vl_Luces_Worth', sa.String(), nullable=True),
    sa.Column('Vp_Luces_Worth', sa.String(), nullable=True),
    sa.Column('Bagolini_Objetivo', sa.String(), nullable=True),
    sa.Column('Bagolini_Subjetivo', sa.String(), nullable=True),
    sa.Column('Mom_Test_Dem_H', sa.String(), nullable=True),
    sa.Column('Mom_Test_Dem_V', sa.String(), nullable=True),
    sa.Column('Mom_Test_Dem_R', sa.String(), nullable=True),
    sa.Column('Mom_Test_Dem_Tipo', sa.Integer(), nullable=True),
    sa.Column('Mom_Test_Dem_Sumatoria', sa.String(), nullable=True),
    sa.Column('Mom_Test_Dem_Observaciones', sa.String(), nullable=True),
    sa.Column('Mom_Test_Dem_Diagnostico', sa.String(), nullable=True),
    sa.Column('Mom_Test_Dem_Plan', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['Mom_Test_Dem_Tipo'], ['opt_tipo_test_dem.id'], ),
    sa.ForeignKeyConstraint(['examen_id'], ['examen.id'], ),
    sa.ForeignKeyConstraint(['idVergencia_Falla_VL'], ['test_adicional_tipo.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('opt_refraccion',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('examen_id', sa.Integer(), nullable=True),
    sa.Column('finalOjoDerecho', sa.String(), nullable=True),
    sa.Column('puntajeFinalOjoDerecho', sa.String(), nullable=True),
    sa.Column('finalOjoIzquierdo', sa.String(), nullable=True),
    sa.Column('puntajeFinalOjoIzquierdo', sa.String(), nullable=True),
    sa.Column('finalAdd', sa.String(), nullable=True),
    sa.Column('puntajeFinalAdd', sa.String(), nullable=True),
    sa.Column('titMus', sa.Float(), nullable=True),
    sa.Column('ishihara', sa.String(), nullable=True),
    sa.Column('AmslerOD', sa.String(), nullable=True),
    sa.Column('AmslerOI', sa.String(), nullable=True),
    sa.Column('dp', sa.String(), nullable=True),
    sa.Column('diagnostico', sa.String(), nullable=True),
    sa.Column('diagnostico1', sa.String(), nullable=True),
    sa.Column('diagnostico2', sa.String(), nullable=True),
    sa.Column('diagnostico3', sa.String(), nullable=True),
    sa.Column('tratamiento', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['examen_id'], ['examen.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('opt_refraccion_estado',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('examen_id', sa.Integer(), nullable=True),
    sa.Column('tipo_estado_id', sa.Integer(), nullable=True),
    sa.Column('ojoDerecho', sa.String(), nullable=True),
    sa.Column('ojoIzquierdo', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['examen_id'], ['examen.id'], ),
    sa.ForeignKeyConstraint(['tipo_estado_id'], ['opt_refraccion_tipo_estado.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('opt_refraccion_vision',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('examen_id', sa.Integer(), nullable=True),
    sa.Column('vlOjoDerechoSC', sa.String(length=250), nullable=True),
    sa.Column('vlOjoIzquierdoSC', sa.String(length=250), nullable=True),
    sa.Column('vlOjoDerechoCC', sa.String(length=250), nullable=True),
    sa.Column('vlOjoIzquierdoCC', sa.String(length=250), nullable=True),
    sa.Column('vpOjoDerechoSC', sa.String(length=250), nullable=True),
    sa.Column('vpOjoIzquierdoSC', sa.String(length=250), nullable=True),
    sa.Column('vpOjoDerechoCC', sa.String(length=250), nullable=True),
    sa.Column('vpOjoIzquierdoCC', sa.String(length=250), nullable=True),
    sa.Column('rxOjoDerecho', sa.String(length=250), nullable=True),
    sa.Column('rxOjoIzquierdo', sa.String(length=250), nullable=True),
    sa.Column('qtOjoDerecho', sa.String(length=250), nullable=True),
    sa.Column('qtOjoIzquierdo', sa.String(length=250), nullable=True),
    sa.Column('atrOjoDerecho', sa.String(length=250), nullable=True),
    sa.Column('atrOjoIzquierdo', sa.String(length=250), nullable=True),
    sa.Column('estOD', sa.String(length=50), nullable=True),
    sa.Column('cylOD', sa.String(length=50), nullable=True),
    sa.Column('ejeOD', sa.String(length=50), nullable=True),
    sa.Column('addOD', sa.String(length=50), nullable=True),
    sa.Column('estOI', sa.String(length=50), nullable=True),
    sa.Column('cylOI', sa.String(length=50), nullable=True),
    sa.Column('ejeOI', sa.String(length=50), nullable=True),
    sa.Column('addOI', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['examen_id'], ['examen.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('opt_refraccion_vision')
    op.drop_table('opt_refraccion_estado')
    op.drop_table('opt_refraccion')
    op.drop_table('opt_ortoptica')
    op.drop_table('opt_oftalmologia')
    op.drop_table('opt_lentes_contacto')
    op.drop_table('tbl_citas')
    op.drop_table('paciente_remitido')
    op.drop_table('medico_horario')
    op.drop_table('examen')
    op.drop_table('tbl_medicos')
    op.drop_table('paciente')
    op.drop_table('appointments')
    op.drop_table('transaccion')
    op.drop_table('test_adicional_tipo')
    op.drop_table('tbl_usuario')
    op.drop_table('tbl_horario')
    op.drop_table('sucursal')
    op.drop_table('opt_tipo_test_dem')
    op.drop_table('opt_refraccion_tipo_estado')
    op.drop_table('opt_ortoptica_tipo')
    op.drop_table('opt_diagnostico')
    op.drop_table('opt__especificaciones')
    op.drop_table('medico_specialidad')
    op.drop_table('admin_usuarios')
    # ### end Alembic commands ###

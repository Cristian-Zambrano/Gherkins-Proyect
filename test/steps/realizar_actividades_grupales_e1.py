from behave import *

#use_step_matcher("re")


@step("que existen espacios públicos disponibles en la ciudad y son")
def step_impl(context, ):
    context.quito = Ciudad(Quito)
    context.la_alameda = EspacioPublico(context.table[0])
    context.la_carolina = EspacioPublico(context.table[1])
    context.bicenterario = EspacioPublico(context.table[2])

    context.Quito.agregar_espacio_publico(context.la_alameda)
    context.Quito.agregar_espacio_publico(context.la_carolina)
    context.Quito.agregar_espacio_publico(context.bicenterario)

    context.la_alameda.agregar_fecha_disponible("2021-06-01", "12:00", "18:00");
    context.la_carolina.agregar_fecha_disponible("2021-06-01", "12:00", "18:00");
    context.bicenterario.agregar_fecha_disponible("2021-06-01", "12:00", "18:00");

    assert context.quito.hay_espacios_publicos_disponibles();


@step('el ciudadano reserve el "Parque_la_Alameda" el "15/01/2025" de "16:00" a "15:00"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: Cuando el ciudadano reserve e l "Parque_la_Alameda" el "15/01/2025" de "16:00" a "15:00"')


@step('existirá una reserva en el "Parque_la_Alameda"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Entonces existirá una reserva en el "Parque_la_Alameda"')


@step("se publicará la reserva en la Agenda Pública.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Y se publicará la reserva en la Agenda Pública.')
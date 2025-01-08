from behave import *

#use_step_matcher("re")


@step("que existen espacios públicos disponibles en la ciudad y son")
def step_impl(context):
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



@step("se publicará la reserva en la Agenda Pública.")
def step_impl(context):
    context.agenda.publicar_reserva(context.reserva)

    assert context.agendaPublica.verificar_la_publicacion_de_la_reserva(context.reserva);
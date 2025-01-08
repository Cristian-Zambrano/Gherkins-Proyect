from behave import *
from app.modelos import *


#use_step_matcher("re")


@step("que existen espacios públicos disponibles en la ciudad y son")
def step_impl(context):
    context.ciudad = Ciudad("Quito")
    context.la_alameda = EspacioPublico(context.table[0])
    context.la_carolina = EspacioPublico(context.table[1])
    context.bicenterario = EspacioPublico(context.table[2])

    context.ciudad.agregar_espacio_publico(context.la_alameda)
    context.ciudad.agregar_espacio_publico(context.la_carolina)
    context.ciudad.agregar_espacio_publico(context.bicenterario)

    context.la_alameda.agregar_fecha_disponible("2021-06-01", "12:00", "18:00");
    context.la_carolina.agregar_fecha_disponible("2021-06-01", "12:00", "18:00");
    context.bicenterario.agregar_fecha_disponible("2021-06-01", "12:00", "18:00");

    assert context.ciudad.hay_espacios_publicos_disponibles();

@step('el ciudadano reserve el "Parque_la_Alameda" el "15/01/2025" de "16:00" a "15:00"')
def step_impl(context, espacio_publico, fecha_reserva, hora_inicio, hora_fin):
    context.agenda = Agenda()
    context.reserva = Reserva(espacio_publico, fecha_reserva, hora_inicio, hora_fin)
    context.agenda.registrar_reserva(context.reserva)
    assert (context.agenda.esta_reserva_en_agenda(context.reserva))

@step("se publicará la reserva en la Agenda Pública.")
def step_impl(context):
    context.agenda.publicar_reserva(context.reserva)
    assert context.agendaPublica.verificar_la_publicacion_de_la_reserva(context.reserva);



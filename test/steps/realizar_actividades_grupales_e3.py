from behave import *




@step('que el ciudadano tiene una reserva en el "Parque la Alameda"')
def step_impl(context, espacio_publico, fecha, hora_inicio, hora_fin):
    context.agenda = Agenda()
    context.reserva = Reserva(espacio_publico, fecha, hora_inicio, hora_fin)
    context.agenda.reservar_espacio_publico(context.reserva)
    assert context.agenda.esta_reserva_en_agenda(context.reserva)



@step("cancele la reserva")
def step_impl(context):
    assert context.agenda.cancelar_reserva(context.reserva)



@step("la reserva será eliminada de la agenda pública\.")
def step_impl(context):
    assert not context.agenda.esta_reserva_en_agenda(context.reserva)

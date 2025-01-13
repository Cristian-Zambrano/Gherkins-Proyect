from behave import *

from app.modelos import Agenda
from app.modelos import Reserva

@step('que el ciudadano tiene una reserva en el "{espacio_publico}"')
def step_impl(context, espacio_publico):
    context.agenda = Agenda()
    fecha_reserva = "15/01/2024"
    hora_inicio = "12:00"
    hora_fin = "18:00"
    invitados = ["jean.cotera@epn.edu", "cristian.sangucho@epn.edu.ec"]
    context.reserva = Reserva(espacio_publico, fecha_reserva, hora_inicio, hora_fin)

    # context.reserva.agregar_invitados(invitados)

    context.reserva.agregar_invitados_a_reserva(invitados)
    context.agenda.registrar_reserva(context.reserva)

    # assert context.agenda.existe_reserva(context.reserva)
    assert context.agenda.esta_reserva_en_agenda(context.reserva)



@step("cancele la reserva")
def step_impl(context):
    context.agenda.cancelar_reserva(context.reserva)

    # assert not context.agenda.existe_reserva(context.reserva)
    assert not context.agenda.esta_reserva_en_agenda(context.reserva)



@step("se enviará una correo de cancelacion de cancelación a los invitados.")
def step_impl(context):
    # context.agenda.enviar_cancelacion(context.reserva)
    assert context.reserva.enviar_cancelacion()

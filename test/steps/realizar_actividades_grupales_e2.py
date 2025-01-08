import locale
from datetime import datetime

from behave import *

from app.modelos import Agenda
from app.modelos import Reserva

#use_step_matcher("re")

@step('el ciudadano reserve el "{espacio_publico}" el "{fecha_reserva}" de "{hora_inicio}" a "{hora_fin}"')
def step_impl(context, espacio_publico, fecha_reserva, hora_inicio, hora_fin):
    context.agenda = Agenda()
    context.reserva = Reserva(espacio_publico, fecha_reserva, hora_inicio, hora_fin)
    context.agenda.registrar_reserva(context.reserva)
    assert (context.agenda.esta_reserva_en_agenda(context.reserva))

@step("se enviará una invitación por correo con los detalles de la reserva.")
def step_impl(context):
    assert context.reserva.enviar_invitacion()


@step('agregue los correos de los invitados "jean.cotera@epn.edu, cristian.sangucho@epn.edu.ec" a la reserva')
def step_impl(context):
    invitados = ["jean.cotera@epn.edu", "cristian.sangucho@epn.edu.ec"]
    context.invitados = invitados
    context.reserva.agregar_invitados_a_reserva(context.invitados)
    assert context.reserva.existen_invitados(context.invitados)
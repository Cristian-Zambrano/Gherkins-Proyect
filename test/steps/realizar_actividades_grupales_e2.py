import locale
from datetime import datetime

from behave import *

use_step_matcher("re")


@step('el ciudadano reserve el "(?P<espacio_publico>.+)" en "(?P<fecha_reserva>.+)" de "(?P<hora_inicio>.+)" a "(?P<hora_fin>.+)"')
def step_impl(context, espacio_publico, fecha_reserva, hora_inicio, hora_fin):
    context.agenda = Agenda()
    context.reserva = Reserva(espacio_publico, fecha_reserva, hora_inicio, hora_fin)
    context.agenda.registrar_reserva(context.reserva)
    assert (context.agenda.esta_reserva_en_agenda(context.reserva))


@step('se enviará una invitación por correo a los "(?P<invitados>.+)" con los detalles de la reserva')
def step_impl(context, invitados):
    assert (invitacion_enviada(context.invitados))
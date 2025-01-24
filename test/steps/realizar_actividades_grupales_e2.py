import locale
from datetime import datetime

from behave import *

from app.modelos import Agenda
from app.modelos import Reserva

#use_step_matcher("re")

@step('el ciudadano reserve el espacio publico "{nombre_espacio_publico}" el "{fecha_reserva}" de "{hora_inicio}" a "{hora_fin}"')
def step_impl(context, nombre_espacio_publico, fecha_reserva, hora_inicio, hora_fin):
    context.ciudadano = Ciudadano("Fernando Do Santos", "1725548763")
    context.espacio_publico = EspacioPublico(nombre_espacio_publico, fecha_reserva, hora_inicio, hora_fin)
    context.ciudadano.reservar_espacio_publico(context.espacio_publico)
    assert (context.cliente.reservar_espacio_publico(context.espacio_publico))

@step('agregue los correos de los invitados "jean.cotera@epn.edu, cristian.sangucho@epn.edu.ec" a la reserva')
def step_impl(context):
    invitados = ["jean.cotera@epn.edu", "cristian.sangucho@epn.edu.ec"]
    context.invitados = invitados
    context.reserva.agregar_invitados_a_reserva(context.invitados)
    assert context.reserva.existen_invitados(context.invitados)

@step("se enviará una invitación por correo con los detalles de la reserva.")
def step_impl(context):
    assert context.reserva.enviar_invitacion()



import locale
from datetime import datetime

from behave import *

from app.modelos import Agenda
from app.modelos import Reserva

#use_step_matcher("re")

#@step('el ciudadano reserve el espacio publico "{nombre_espacio_publico}" el "{fecha_reserva}" de "{hora_inicio}" a "{hora_fin}"')
@step('el ciudadano reserve el "{espacio_publico}" el "{fecha_reserva}" de "{hora_inicio}" a "{hora_fin}"')
def step_impl(context, espacio_publico, fecha_reserva, hora_inicio, hora_fin):
        #context.agenda = Agenda() esto se puede omitir o no xd
        #context.reserva.crear_reserva(context.cliente, context.espacio_publico) esto se puede omitir
        #context.agenda.anadir_reserva(contex.reserva) esto se puede omitir
        #assert (context.agenda.esta_reserva_en_agenda(context.reserva)) esto se puede omitir
    #context.ciudadano = Ciudadano("Fernando Do Santos", "1725548763")
    #context.espacio_publico = EspacioPublico(nombre_espacio_publico, fecha_reserva, hora_inicio, hora_fin)
    #contex.ciudadano.reservar_espacio_publico(context.espacio_publico)
    #assert (contex.cliente.reservar_espacio_publico(context.espacio_publico)) no se si poner como codigos de confirmacion
    context.agenda = Agenda()
    context.reserva = Reserva(espacio_publico, fecha_reserva, hora_inicio, hora_fin)
    context.agenda.registrar_reserva(context.reserva)
    assert (context.agenda.esta_reserva_en_agenda(context.reserva))

@step('agregue los correos de los invitados "jean.cotera@epn.edu, cristian.sangucho@epn.edu.ec" a la reserva')
def step_impl(context):
    invitados = ["jean.cotera@epn.edu", "cristian.sangucho@epn.edu.ec"]
    context.invitados = invitados
    context.reserva.agregar_invitados_a_reserva(context.invitados)
    assert context.reserva.existen_invitados(context.invitados)

@step("se enviará una invitación por correo con los detalles de la reserva.")
def step_impl(context):
    assert context.reserva.enviar_invitacion()



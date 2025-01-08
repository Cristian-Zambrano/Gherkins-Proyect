from behave import *

@step("se enviará una correo de cancelacion de cancelación a los invitados.")
def step_impl(context):
    assert not context.agenda.esta_reserva_en_agenda(context.reserva)

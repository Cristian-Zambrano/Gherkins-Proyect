from behave import *

use_step_matcher("re")


@step("cancele la reserva")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Cuando cancele la reserva')


@step("la reserva será eliminada")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Entonces la reserva será eliminada')


@step("se enviará una correo de cancelacion de cancelación a los invitados\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Y se enviará una correo de cancelacion de cancelación a los invitados.')
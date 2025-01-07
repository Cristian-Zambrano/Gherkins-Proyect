from behave import *

use_step_matcher("re")


@step('que el ciudadano tiene una reserva en el "Parque la Alameda"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Dado que el ciudadano tiene una reserva en el "Parque la Alameda"')


@step("la reserva será eliminada de la agenda pública\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Entonces la reserva será eliminada de la agenda pública.')
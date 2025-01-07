from behave import *

use_step_matcher("re")


@step("que existen espacios públicos disponibles en la ciudad y son")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Dado que existen espacios públicos disponibles en la ciudad y son
                              | Parque
    la
    Alameda |
    | La
    Carolina |
    | Bicentenario | ')


@step('existirá una reserva en el "Parque la Alameda"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Entonces existirá una reserva en el "Parque la Alameda"')


@step('existirá una reserva en el "Parque la Alameda"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Entonces existirá una reserva en el "Parque la Alameda"')


@step("se publicará la reserva en la Agenda Pública\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Y se publicará la reserva en la Agenda Pública.')
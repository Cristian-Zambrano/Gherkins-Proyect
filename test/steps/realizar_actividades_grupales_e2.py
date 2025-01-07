from behave import *

use_step_matcher("re")


@step('el ciudadano reserve el "Parque la Alameda" el "Lunes 15 de enero de 2024" de "16:00" a "15:00"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: Cuando el ciudadano reserve el "Parque la Alameda" el "Lunes 15 de enero de 2024" de "16:00" a "15:00"')


@step("la reserva tenga como invitados a")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Y la reserva tenga como invitados a
                              | jean.cotera @ epn.edu |
                              | cristian.sangucho @ epn.edu.ec | ')


@step("se enviará una invitación a los invitados con los detalles de la reserva")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Y se enviará una invitación a los invitados con los detalles de la reserva')


@step("se enviará una invitación a los invitados con los detalles de la reserva")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Y se enviará una invitación a los invitados con los detalles de la reserva')
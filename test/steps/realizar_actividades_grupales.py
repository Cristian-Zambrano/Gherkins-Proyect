from behave import *

use_step_matcher("re")


@step('que esta disponible el "(?P<espacio_publico>.+)" en los "(?P<espacios_publicos>.+)" de la ciudad')
def step_impl(context, espacio_publico, espacios_publicos):
    """
    :type context: behave.runner.Context
    :type espacio_publico: str
    :type espacios_publicos: str
    """
    raise NotImplementedError(
        u'STEP: Dado que esta disponible un "<espacio_publico>" en los "<espacios_publicos>" de la ciudad')


@step('que el "(?P<espacio_publico>.+)" tenga una disponibilidad el "(?P(?P<dia_semana>.+).+)" de "(?P<hora_inicio>.+)" a "(?P(?P<dia_semana>.+).+)" "(?P<hora_fin>.+)"')
def step_impl(context, espacio_publico, dia_semana, hora_inicio, dia_semana1, hora_fin):
    """
    :type context: behave.runner.Context
    :type espacio_publico: str
    :type dia_semana: str
    :type hora_inicio: str
    :type hora_fin: str
    """
    raise NotImplementedError(
        u'STEP: Y que el "<espacio_publico>" tenga una disponibilidad el "<dia_semana>" de "<hora_inicio>" a "<dia_semana>" "<hora_fin>"')


@step('el ciudadano quiera realizar la actividad en "(?P<espacio_publico>.+)"')
def step_impl(context, espacio_publico):
    """
    :type context: behave.runner.Context
    :type espacio_publico: str
    """
    raise NotImplementedError(u'STEP: Cuando el ciudadano quiera realizar la actividad en "<espacio_publico>"')


@step(
    'seleccione el "(?P(?P<dia_semana>.+).+)" de "(?P<hora_inicio>.+)" a "(?P(?P<dia_semana>.+).+)" "(?P<hora_fin>.+)"')
def step_impl(context, dia_semana, hora_inicio, dia_semana1, hora_fin):
    """
    :type context: behave.runner.Context
    :type dia_semana: str
    :type hora_inicio: str
    :type hora_fin: str
    """
    raise NotImplementedError(u'STEP: Y seleccione el "<dia_semana>" de "<hora_inicio>" a "<dia_semana>" "<hora_fin>"')


@step('el ciudadano tendrá una reserva de "(?P<espacio_publico>.+)"')
def step_impl(context, espacio_publico):
    """
    :type context: behave.runner.Context
    :type espacio_publico: str
    """
    raise NotImplementedError(u'STEP: Entonces el ciudadano tendrá una reserva de "<espacio_publico>"')


@step("se publicará la actividad en la agenda de actividades públicas")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Y se publicará la actividad en la agenda de actividades públicas')


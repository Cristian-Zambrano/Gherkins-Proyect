#language: es
Característica: Realizar actividades grupales
  Como ciudadano ecuatoriano
  Quiero realizar actividades grupales en un espacio publico
  Para socializar actividades en conjunto con otros ciudadanos


#  Escenario: Participar en actividades públicas
#    Dado que existen 3 espacios públicos en la ciudad:
#      | Parque Alameda      |
#      | Parque Bicentenario |
#      | Estadio Liga        |
#    Y que "*Parque Alameda*" está disponible el día "*Lunes*" de "*15:00*" a "*Lunes*", "*17:00*"
#    Y que "*Parque Bicentenario*" está disponible el día "*Martes*" de "*14:00*" a "*Martes*", "*16:00*"
#    Y que "*Estadio Liga*" está disponible el día "*Miércoles*" de "*15:00*" a "*Miércoles*", "*19:00*"
#    Cuando el ciudadano quiera realizar la actividad en "*Parque Alameda*"
#    Entonces el ciudadano tendrá una reserva de "*Parque Alameda*"
#    Y se publicará la actividad en la agenda de actividades públicas


  Esquema del escenario: espacios publicos
    Dado que esta disponible el "<espacio_publico>" en los "<espacios_publicos>" de la ciudad
    Y que el "<espacio_publico>" tenga una disponibilidad el "<dia_semana>" de "<hora_inicio>" a "<dia_semana>" "<hora_fin>"
    Cuando el ciudadano quiera realizar la actividad en "<espacio_publico>"
    Y seleccione el "<dia_semana>" de "<hora_inicio>" a "<dia_semana>" "<hora_fin>"
    Entonces el ciudadano tendrá una reserva de "<espacio_publico>"
    Y se publicará la actividad en la agenda de actividades públicas
    Ejemplos:
      | espacios_publicos                                         | espacio_publico       | dia_semana  | hora_inicio | dia_semana  | hora_fin |
      | ["Parque Alameda", "Parque Bicentenario", "Estadio Liga"] | "Parque Alameda"      | "Lunes"     | "15:00"     | "Lunes"     | "17:00"  |
      | ["Parque Alameda", "Parque Bicentenario", "Estadio Liga"] | "Parque Bicentenario" | "Martes"    | "14:00"     | "Martes"    | "16:00"  |
      | ["Parque Alameda", "Parque Bicentenario", "Estadio Liga"] | "Estadio Liga"        | "Miércoles" | "15:00"     | "Miércoles" | "19:00"  |

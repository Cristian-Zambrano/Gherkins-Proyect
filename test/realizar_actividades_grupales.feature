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

  Escenario: reserva de espacio disponible para actividad pública
   Dado que existen espacios públicos en la ciudad y son 
      | Parque la Alameda |
      | La Carolina |
       | Bicentenario |
   Cuando el ciudadano reserve el Parque la Alameda el Lunes 15 de enero de 2024 de 16:00 a 15:00
   Entonces existirá una reserva en el Parque la Alameda
   Y se publicará la reserva en la Agenda Pública.

  



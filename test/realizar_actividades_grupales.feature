#language: es
Característica: Realizar actividades grupales
  Como ciudadano
  Quiero realizar actividades grupales en un espacio pública
  Para socializar actividades en conjunto con otros ciudadanos

  Escenario: reserva de espacio disponible para actividad pública
    Dado que existen espacios públicos disponibles en la ciudad y son
      | Nombre            |
      | Parque la Alameda |
      | La Carolina       |
      | Bicentenario      |
    Cuando el ciudadano reserve el "Parque la Alameda" el "15/01/2024" de "16:00" a "15:00"
    Entonces se publicará la reserva en la Agenda Pública.

  Escenario: Reserva de un espacio público para una actividad privada
    Dado que existen espacios públicos disponibles en la ciudad y son
      | Parque la Alameda |
      | La Carolina       |
      | Bicentenario      |
    Cuando el ciudadano reserve el "Parque la Alameda" el "15/01/2024" de "16:00" a "15:00"
    Entonces se enviará una invitación por correo a "jean.cotera@epn.edu, cristian.sangucho@epn.edu.ec" con los detalles de la reserva

#  Esquema del escenario: Reserva de un espacio público para una actividad privada
#    Dado que existen espacios públicos disponibles en la ciudad y son
#      | Parque la Alameda |
#      | La Carolina       |
#      | Bicentenario      |
#    Cuando el ciudadano reserve el "<espacio_publico>" en "<fecha_reserva>" de "<hora_inicio>" a "<hora_fin>"
#    Entonces se enviará una invitación por correo a los "<invitados>" con los detalles de la reserva
#
#    Ejemplos:
#      | espacio_publico   | fecha_reserva | hora_inicio | hora_fin | invitados                                           |
#      | Parque la Alameda | 15/01/2025    | 16:00       | 15:00    | jean.cotera@epn.edu, cristian.sangucho@epn.edu.ec   |
#      | La Carolina       | 16/01/2025    | 10:00       | 12:00    | maria.lopez@correo.com, pedro.garcia@gmail.com      |
#      | Bicentenario      | 17/0/2025     | 09:00       | 11:30    | ana.martinez@correo.edu.ec, jorge.perez@hotmail.com |


  Escenario: Cancelar reserva de actividad pública
    Dado que el ciudadano tiene una reserva en el "Parque la Alameda"
    Cuando cancele la reserva
    Entonces la reserva será eliminada de la agenda pública.

  Escenario: Cancelar reserva de actividad privada
    Dado que el ciudadano tiene una reserva en el "Parque la Alameda"
    Cuando cancele la reserva
    Entonces se enviará una correo de cancelacion de cancelación a los invitados.
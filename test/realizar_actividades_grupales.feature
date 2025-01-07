#language: es
Característica: Realizar actividades grupales
  Como ciudadano
  Quiero realizar actividades grupales en un espacio pública
  Para socializar actividades en conjunto con otros ciudadanos

  Escenario: reserva de espacio disponible para actividad pública
    Dado que existen espacios públicos disponibles en la ciudad y son
      | Parque la Alameda |
      | La Carolina       |
      | Bicentenario      |
    Cuando el ciudadano reserve el "Parque_la_Alameda" el "15/01/2025" de "16:00" a "15:00"
    Entonces existirá una reserva en el "Parque_la_Alameda"
    Y se publicará la reserva en la Agenda Pública.

#  Escenario: Reserva de un espacio público para una actividad privada
#    Dado que existen espacios públicos disponibles en la ciudad y son
#      | Parque la Alameda |
#      | La Carolina       |
#      | Bicentenario      |
#    Cuando el ciudadano reserve el "Parque la Alameda" el "Lunes 15 de enero de 2024" de "16:00" a "15:00"
#    Y la reserva tenga como invitados a 'jean.cotera@epn.edu, cristian.sangucho@epn.edu.ec'
#    Entonces existirá una reserva en el "Parque la Alameda"
#    Y se enviará una invitación a los invitados con los detalles de la reserva

    Esquema del escenario: Reserva de un espacio público para una actividad privada
    Dado que existen espacios públicos disponibles en la ciudad y son
      | Espacio           |
      | Parque la Alameda |
      | La Carolina       |
      | Bicentenario      |
    Cuando el ciudadano reserve el "<espacio_publico>" el "<fecha_reserva>" de "<hora_inicio>" a "<hora_fin>"
    Y la reserva tenga como invitados a '<invitados>'
    Entonces se enviará una invitación a los invitados con los detalles de la reserva

    Ejemplos:
      | espacio_reservado | fecha_reserva                        | hora_inicio | hora_fin | invitados                                           |
      | Parque la Alameda | Lunes 15 de enero de 2024     | 16:00       | 15:00    | jean.cotera@epn.edu, cristian.sangucho@epn.edu.ec   |
      | La Carolina       | Martes 16 de enero de 2024    | 10:00       | 12:00    | maria.lopez@correo.com, pedro.garcia@gmail.com      |
      | Bicentenario      | Miércoles 17 de enero de 2024 | 09:00       | 11:30    | ana.martinez@correo.edu.ec, jorge.perez@hotmail.com |


  Escenario: Cancelar reserva de actividad pública
    Dado que el ciudadano tiene una reserva en el "Parque la Alameda"
    Cuando cancele la reserva
    Entonces la reserva será eliminada de la agenda pública.

  Escenario: Cancelar reserva de actividad privada
    Dado que el ciudadano tiene una reserva en el "Parque la Alameda"
    Cuando cancele la reserva
    Entonces la reserva será eliminada
    Y se enviará una correo de cancelacion de cancelación a los invitados.
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
    Cuando el ciudadano reserve el "Parque la Alameda" el "Lunes 15 de enero de 2024" de "16:00" a "15:00"
    Entonces existirá una reserva en el "Parque la Alameda"
    Y se publicará la reserva en la Agenda Pública.

  Escenario: Reserva de un espacio público para una actividad privada
    Dado que existen espacios públicos disponibles en la ciudad y son
      | Parque la Alameda |
      | La Carolina       |
      | Bicentenario      |
    Cuando el ciudadano reserve el "Parque la Alameda" el "Lunes 15 de enero de 2024" de "16:00" a "15:00"
    Y la reserva tenga como invitados a
      | jean.cotera@epn.edu          |
      | cristian.sangucho@epn.edu.ec |
    Entonces existirá una reserva en el "Parque la Alameda"
    Y se enviará una invitación a los invitados con los detalles de la reserva

  Escenario: Cancelar reserva de actividad pública
    Dado que el ciudadano tiene una reserva en el "Parque la Alameda"
    Cuando cancele la reserva
    Entonces la reserva será eliminada de la agenda pública.

  Escenario: Cancelar reserva de actividad privada
    Dado que el ciudadano tiene una reserva en el "Parque la Alameda"
    Cuando cancele la reserva
    Entonces la reserva será eliminada
    Y se enviará una correo de cancelacion de cancelación a los invitados.
from typing import List
from email.message import EmailMessage
import smtplib
import pandas as pd


class Ciudad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.espacios_publicos: List[EspacioPublico] = []

    def agregar_espacio_publico(self, espacio_publico):
        self.espacios_publicos.append(espacio_publico)

    def hay_espacios_publicos_disponibles(self):
        for espacio_publico in self.espacios_publicos:
            if espacio_publico.tiene_fechas_disponibles():
                return True
        return False


class EspacioPublico:
    def __init__(self, nombre):
        self.nombre = nombre
        self.fechas_disponibles = []

    def agregar_fecha_disponible(self, fecha, hora_inicio, hora_fin):
        self.fechas_disponibles = pd.date_range(start=f"{fecha} {hora_inicio}", end=f"{fecha} {hora_fin}", freq='1H')

    def tiene_fechas_disponibles(self):
        if len(self.fechas_disponibles) > 0:
            return True
        return False


class Agenda:
    def __init__(self):
        self.reservas = []

    def registrar_reserva(self, reserva):
        self.reservas.append(reserva)


class Reserva:
    def __init__(self, espacio_publico, fecha_reserva, hora_inicio, hora_fin):
        self.espacio_publico = espacio_publico
        self.fecha_reserva = fecha_reserva
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.invitados = []

    def existen_invitados(self, invitados):
        return set(invitados) == set(self.invitados)

    def agregar_invitados_a_reserva(self, invitados):
        self.invitados = invitados

    def enviar_invitacion(self):
        for invitado in self.invitados:
            remitente = "cristian-13-700@outlook.com"
            destinatario = invitado
            mensaje = self.__str__()
            email = EmailMessage()
            email["From"] = remitente
            email["To"] = destinatario
            email["Subject"] = "Correo de prueba"
            email.set_content(mensaje)
            smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
            smtp.starttls()
            smtp.login(remitente, "FAMILIA123")
            smtp.sendmail(remitente, destinatario, email.as_string())
            smtp.quit()



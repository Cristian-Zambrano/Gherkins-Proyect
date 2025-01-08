from typing import List

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
        self.reservas_publicadas: List[Reserva] = []

    def publicar_reserva(self, reserva):
        self.publicar(reserva)
        self.reservas_publicadas.append(reserva)

    def publicar(self, reserva):
        # publicanding...
        pass

    def verificar_la_publicacion_de_la_reserva(self, reserva):
        for reserva_publicada in self.reservas_publicadas:
            if reserva_publicada.equals(reserva):
                return True
        return False
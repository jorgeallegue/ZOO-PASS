from enum import Enum, auto

class TipoEntrada(Enum):
    BEBE = auto()
    NIÑO = auto()
    ADULTO = auto()
    JUBILADO = auto()


class Entrada:
    def __init__(self, edad: int):
        if edad <= 2:
            self.tipo = TipoEntrada.BEBE
            self.precio = 0
        elif edad <= 13:
            self.tipo = TipoEntrada.NIÑO
            self.precio = 14
        elif edad <= 65:
            self.tipo = TipoEntrada.ADULTO
            self.precio = 23
        else:
            self.tipo = TipoEntrada.JUBILADO
            self.precio = 18
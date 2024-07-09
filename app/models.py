from enum import Enum, auto

class TipoEntrada(Enum):
    BEBE = auto()
    NIÑO = auto()
    ADULTO = auto()
    JUBILADO = auto()

class Entrada:

    def __init__(self, edad: int):
        if edad <0:
            self.__validate_edad(edad)
        elif edad <= 2:
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
    def __validate_edad(self, edad):
        if edad < 0:
            raise ValueError("La edad no debe ser negativa")

class Grupo_Entrada:
    def __init__(self):
        self.total = 0
        self.num_entradas = 0
        self.tipos_entrada = {
            TipoEntrada.BEBE: 0,
            TipoEntrada.NIÑO: 0,
            TipoEntrada.ADULTO: 0,
            TipoEntrada.JUBILADO: 0
        }

    def add_entrada(self, edad):
        """
        en funcion de la edad, crear e incrementar el contador de 
        entradas.
        Con el precio de la entrada nueva incrementar el total
        """
        nueva_entrada = Entrada(edad)
        self.num_entradas += 1
        self.total += nueva_entrada.precio

        self.tipos_entrada[nueva_entrada.tipo] += 1    
    
    def cantidad_entrada_por_tipo(self, tipo: TipoEntrada):
        return self.tipos_entrada[tipo]


#importar el modulo enum (los modulos contienen funciones, clases  y variables. objetivo es poder organizar mi codigo en partes reutilizables y bien estructuradas)
#Enum permite ENUMERATE un conjunto de valores con nombres significativos asociandolos entre ellos
#auto permite asignar automaticamente valores únicos a los miembros de una enumeración(de manera consecutiva y unica) sin preocuparme de tener que asignar manualmente cada uno. BEBÉ = 1; NIÑO = 2; ADULTO = 3...etc
#IMPORTANTE: CONOCER EL COMPORTAMIENTO DE MÁS MÓDULOS PARA FACILITAR EL TRABAJO.
from enum import Enum, auto

#Declaro una nueva clase con nombre "TipoDeEntrada". Extiendo funcionalidad y comportamiento de TipoDeEntrada con (Enum) después de TipoDeEntrada
#Enum proporciona la estructura y el comportamiento de TipoDeEntrada (osea: enumerar)
#auto() esta sin argumentos porque su comportamiento predeterminado ya esta definido para asignar valores unicos automaticamente
class TipoDeEntrada(Enum):
    BEBE = auto()
    NIÑO = auto()
    ADULTO = auto()
    JUBILADO = auto()

#con la sintaxis class Entrada: defino la estructura básica de la clase (podré definir metodos (funciones asociadas a la clase))
class Entrada:
# el __init__ es un contructor que se llama automaticamente cuando se crea una nueva instancia(objeto) de la clase "Entrada"
#el proposito de __init__ es inicializar los atributos de la instancia con los valores proporcionados
#"self" se utiliza para acceder a los atributos y metods de la instancia dentro de la clase.
#tipo: TipoDeEntrada es el primer parametro del constructor. TipoDeEntrada hace referencia a otra clase (que en este caso esta enumerada por enum)
#precio: int es el segundo parametro del constructor y especifica el precio numerico de la entrada.
    def __init__(self, tipo: TipoDeEntrada, precio: int):
        self.tipo = tipo # aqui asigno el valor del parametro tipo  al atributo self.tipo. Objetivo: que cada instancia de Entrada tenga su propio atributo tipo que puede ser uno de los valores definidos en TipoDeEntrada (p.ejemplo TipoDeEntrada.BEBE)
        self.precio = precio #aqui asigno el valor del parametro precio al atributo self.precio. Cada instancia de entrada tendra su precio especifico.
    # con @classmethod creo instancias predefinidas. Los métodos crear_bebe, crear 
    #ventajas: 1. puedo crear instacias de la clase de manera modular. 2. puedo crear instancias con valores predefinidos 3. facil de entender y facil de mantener
    @classmethod # @classmethod es un metodo de la clase
    def definir_bebe(Entrada): #definir_bebe es un metodo de clase que crea instancias especificas de Entrada con configuraciones predefinidas por tipo y precio
        return Entrada(TipoDeEntrada.BEBE, 0) #esto devuelve 1 instancia de entrada con el TipoDeEntrada.BEBE y con un precio de 0

    @classmethod
    def definir_niño(Entrada): # resumen: crea y devuelve una instancia del tipo NIÑO con precio 23
        return Entrada(TipoDeEntrada.NIÑO, 14)

    @classmethod
    def definir_adulto(Entrada):
        return Entrada(TipoDeEntrada.ADULTO, 23)

    @classmethod
    def definir_jubilado(Entrada):
        return Entrada(TipoDeEntrada.JUBILADO, 18)

    @classmethod
    def crear_instancia_de_entrada_por_edad(Entrada, edad: int): #determina el tipo de entrada basado en la edad proporcionada y devuelve una instancia de Entrada basada en la edad proporcionada
        if edad < 0:
            raise ValueError("La edad no debe ser negativa")
        elif edad <= 2:
            return Entrada.definir_bebe() 
        elif edad <= 13:
            return Entrada.definir_niño()
        elif edad <= 65:
            return Entrada.definir_adulto()
        else:
            return Entrada.definir_jubilado()

class Grupo_Entrada: # gestor de entradas. cuenta y almacena info sobre diferentes tipos de entrada que se han vendido
    def __init__(self): # es el constructor de la clase Grupo_Entrada. cuando creo una nueva instancia de Grupo_entrada el constructor se llama automaticamente  para inicializar los atributos de esta instancia.self es la instancia actual de la clase
        self.total = 0  # inicializa el atributo total se la instacia actual self a 0. este atributo se usa para tener un segumeinto del total acumulado del valor asociado a las entradas
        self.num_entradas = 0 # inicializa el atributo num_entradas a 0. se usa para contar el número total de entradas gestionadas por esta instancia de GrupoEntrada.
        self.tipos_entrada = { # Inicializa el atributo tipos_entrada como un diccionario. Este diccionario utiliza los valores de TipoEntrada (como TipoEntrada.BEBE, TipoEntrada.NIÑO, etc.) como claves y los inicializa a 0. Este atributo podría usarse para mantener un seguimiento de cuántas entradas de cada tipo se han vendido o gestionado
            TipoDeEntrada.BEBE: 0,
            TipoDeEntrada.NIÑO: 0,
            TipoDeEntrada.ADULTO: 0,
            TipoDeEntrada.JUBILADO: 0
        }
        self.entradas = [] #Inicializa el atributo entradas como una lista vacía. Este atributo podría usarse para almacenar objetos individuales de tipo Entrada u objetos similares que representan las entradas vendidas o gestionadas por esta instancia de GrupoEntrada.

    def add_entrada(self, entrada: Entrada): #esta funcion agrega una nueva entrada a la instancia Grupo_Entrada (actualizando los contadores)
        self.num_entradas = self.num_entradas + 1  #incrementa el contador de entradas
        self.total = self.total + entrada.precio #actualiza el total acumulado. el precio de la nueva entrada se suma al total acumulado
        self.tipos_entrada[entrada.tipo] =  self.tipos_entrada[entrada.tipo] + 1 # El contador del tipo específico de la entrada se incrementa en 1 en el diccionario tipos_entrada.
        self.entradas.append(entrada)   #La nueva entrada se agrega a la lista entradas
    # Utiliza el diccionario tipos_entrada para obtener el número de entradas del tipo especificado y lo devuelve.
    def cantidad_entrada_por_tipo(self, tipo: TipoDeEntrada): # Esta función devuelve la cantidad de entradas vendidas de un tipo específico.
        return self.tipos_entrada[tipo] #tipo es un valor de TipoDeEntrada, que especifica el tipo de entrada del cual queremos conocer la cantidad.
    
    def subtotal_tipo(self, tipo: TipoDeEntrada) -> int:# Esta función calcula el total de ingresos generados por un tipo específico de entrada.
                                                        #Parámetro: tipo es un valor de TipoDeEntrada, que especifica el tipo de entrada del cual queremos calcular el subtotal.
        subtotal = sum(entrada.precio for entrada in self.entradas if entrada.tipo == tipo) #Utiliza una expresión generadora para sumar los precios de todas las entradas en la lista entradas que coincidan con el tipo especificado.
        return subtotal
    
    def __str__(self): #constructor de la clase
        return (f"Total entradas: {self.num_entradas}, "
                f"Total ingresos: {self.total}, "
                f"Entradas por tipo: {self.tipos_entrada}")
    #Utiliza una f-string para formatear una cadena que contiene el número total de entradas (num_entradas), el total de ingresos (total) y el diccionario de tipos de entrada (tipos_entrada).


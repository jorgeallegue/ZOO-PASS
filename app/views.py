from app.models import Entrada, Grupo_Entrada, TipoDeEntrada

def obtener_cantidad_entradas():
    try:
        cantidad_bebes = int(input("Ingrese la cantidad de entradas para bebés: "))
        cantidad_niños = int(input("Ingrese la cantidad de entradas para niños: "))
        cantidad_adultos = int(input("Ingrese la cantidad de entradas para adultos: "))
        cantidad_jubilados = int(input("Ingrese la cantidad de entradas para jubilados: "))
        return cantidad_bebes, cantidad_niños, cantidad_adultos, cantidad_jubilados
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return obtener_cantidad_entradas()

def mostrar_resumen(grupo):
    print(grupo)
    for tipo in TipoDeEntrada:
        print(f"Cantidad de entradas para {tipo.name}: {grupo.cantidad_entrada_por_tipo(tipo)}")
        print(f"Subtotal para {tipo.name}: {grupo.subtotal_tipo(tipo)}")
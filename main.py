# Importar las clases del archivo models.py
from app.models import Entrada, Grupo_Entrada, TipoDeEntrada

def main():
    # Crear un grupo de entradas
    grupo = Grupo_Entrada()
    
    # Pedir al usuario la cantidad de entradas por tipo
    cantidad_bebe = int(input("Ingrese la cantidad de entradas para bebé: "))
    cantidad_niño = int(input("Ingrese la cantidad de entradas para niño: "))
    cantidad_adulto = int(input("Ingrese la cantidad de entradas para adulto: "))

    # Añadir las entradas solicitadas al grupo
    for _ in range(cantidad_bebe):
        grupo.add_entrada(Entrada.definir_bebe())
    
    for _ in range(cantidad_niño):
        grupo.add_entrada(Entrada.definir_niño())
    
    for _ in range(cantidad_adulto):
        grupo.add_entrada(Entrada.definir_adulto())

    # Mostrar el resumen del grupo de entradas
    print(grupo)

    # Mostrar cantidad de entradas por tipo
    for tipo in TipoDeEntrada:
        print(f"Cantidad de entradas para {tipo.name}: {grupo.cantidad_entrada_por_tipo(tipo)}")

    # Mostrar subtotal por tipo de entrada
    for tipo in TipoDeEntrada:
        print(f"Subtotal para {tipo.name}: {grupo.subtotal_tipo(tipo)}")

if __name__ == "__main__":
    main()
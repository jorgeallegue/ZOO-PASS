from models import Entrada, Grupo_Entrada, TipoDeEntrada
from views import obtener_cantidad_entradas, mostrar_resumen

def main():
    grupo = Grupo_Entrada()  # Crear un grupo de entradas
    
    while True:
        edad_str = input("Ingrese la edad del visitante (o clic intro para terminar): ")
        
        if edad_str.lower() == '':
            break

        try:
            edad = int(edad_str)
        except ValueError:
            print("Por favor ingrese un número entero válido o clic intro para terminar.")
            continue
        
        # Determinar el tipo de entrada según la edad ingresada
        entrada = Entrada.crear_instancia_de_entrada_por_edad(edad)
        grupo.add_entrada(entrada)

    # Mostrar el resumen del grupo de entradas
    mostrar_resumen(grupo)

    # Mostrar total de entradas vendidas
    total_entradas_vendidas = grupo.num_entradas
    print(f"Total de entradas vendidas: {total_entradas_vendidas}")

    # Calcular y mostrar coste total de todas las entradas
    coste_total = sum(entrada.precio for entrada in grupo.entradas)
    print(f"COSTE TOTAL DE TODAS LAS ENTRADAS: {coste_total}")

    # Mostrar cantidad de entradas por tipo
    for tipo in TipoDeEntrada:
        print(f"Cantidad de entradas para {tipo.name}: {grupo.cantidad_entrada_por_tipo(tipo)}")

    # Mostrar subtotal por tipo de entrada
    for tipo in TipoDeEntrada:
        print(f"Subtotal para {tipo.name}: {grupo.subtotal_tipo(tipo)}")

if __name__ == "__main__":
    main()
from app.models import Entrada, TipoDeEntrada, Grupo_Entrada
import pytest

# Corrige el constructor de la clase Entrada en las pruebas
def test_crear_entrada():
    entrada = Entrada.crear_instancia_de_entrada_por_edad(12)
    assert entrada.tipo == TipoDeEntrada.NIÑO
    assert entrada.precio == 14

    entrada = Entrada.crear_instancia_de_entrada_por_edad(35)
    assert entrada.tipo == TipoDeEntrada.ADULTO
    assert entrada.precio == 23

    entrada = Entrada.crear_instancia_de_entrada_por_edad(70)
    assert entrada.tipo == TipoDeEntrada.JUBILADO
    assert entrada.precio == 18

    entrada = Entrada.crear_instancia_de_entrada_por_edad(1)
    assert entrada.tipo == TipoDeEntrada.BEBE
    assert entrada.precio == 0

def test_crear_entrada_edad_negativa_error():
    with pytest.raises(ValueError):
        Entrada.crear_instancia_de_entrada_por_edad(-2)
    """
    Esto sería equivalente a lo de arriba
    try:
        entrada = Entrada.crear_instancia_de_entrada_por_edad(-2)
        assert False, "No ha saltado ValueError"
    except ValueError:
        assert True 
    """

def test_crear_grupo_entradas():
    grupo = Grupo_Entrada()
    assert grupo.total == 0
    assert  grupo.num_entradas == 0

def test_añadir_entradas_a_grupos():
    grupo = Grupo_Entrada()
    grupo.add_entrada(Entrada.crear_instancia_de_entrada_por_edad(35))
    assert grupo.num_entradas == 1
    assert grupo.total == 23
    
    grupo.add_entrada(Entrada.crear_instancia_de_entrada_por_edad(12))
    assert grupo.num_entradas == 2
    assert grupo.total == 37

    grupo.add_entrada(Entrada.crear_instancia_de_entrada_por_edad(70))
    assert grupo.num_entradas == 3
    assert grupo.total == 55

    grupo.add_entrada(Entrada.crear_instancia_de_entrada_por_edad(2))
    assert grupo.num_entradas == 4
    assert grupo.total == 55  # Corrige aquí el precio de entrada de BEBÉ (debería ser 0)


def test_cantidad_entrada_por_tipo():
    grupo = Grupo_Entrada()
    grupo.add_entrada(Entrada.crear_instancia_de_entrada_por_edad(10))
    grupo.add_entrada(Entrada.crear_instancia_de_entrada_por_edad(70))
    grupo.add_entrada(Entrada.crear_instancia_de_entrada_por_edad(35))
    grupo.add_entrada(Entrada.crear_instancia_de_entrada_por_edad(2))

    assert grupo.cantidad_entrada_por_tipo(TipoDeEntrada.NIÑO) == 1
    assert grupo.cantidad_entrada_por_tipo(TipoDeEntrada.JUBILADO) == 1
    assert grupo.cantidad_entrada_por_tipo(TipoDeEntrada.ADULTO) == 1
    assert grupo.cantidad_entrada_por_tipo(TipoDeEntrada.BEBE) == 1

def test_subtotal_por_tipo():
    grupo = Grupo_Entrada()
    grupo.add_entrada(Entrada.crear_instancia_de_entrada_por_edad(10))
    assert grupo.subtotal_tipo(TipoDeEntrada.NIÑO) == 14

def test_entrada_transiciones():
    # Test for edge ages
    entrada = Entrada.crear_instancia_de_entrada_por_edad(2)
    assert entrada.tipo == TipoDeEntrada.BEBE
    assert entrada.precio == 0

    entrada = Entrada.crear_instancia_de_entrada_por_edad(3)
    assert entrada.tipo == TipoDeEntrada.NIÑO
    assert entrada.precio == 14

    entrada = Entrada.crear_instancia_de_entrada_por_edad(13)
    assert entrada.tipo == TipoDeEntrada.NIÑO
    assert entrada.precio == 14

    entrada = Entrada.crear_instancia_de_entrada_por_edad(14)
    assert entrada.tipo == TipoDeEntrada.ADULTO
    assert entrada.precio == 23

    entrada = Entrada.crear_instancia_de_entrada_por_edad(65)
    assert entrada.tipo == TipoDeEntrada.ADULTO
    assert entrada.precio == 23

    entrada = Entrada.crear_instancia_de_entrada_por_edad(66)
    assert entrada.tipo == TipoDeEntrada.JUBILADO
    assert entrada.precio == 18

def test_repr_grupo_entradas():
    grupo = Grupo_Entrada()
    assert str(grupo) == "Total entradas: 0, Total ingresos: 0, Entradas por tipo: {<TipoDeEntrada.BEBE: 1>: 0, <TipoDeEntrada.NIÑO: 2>: 0, <TipoDeEntrada.ADULTO: 3>: 0, <TipoDeEntrada.JUBILADO: 4>: 0}"

    grupo.add_entrada(Entrada.crear_instancia_de_entrada_por_edad(12))
    grupo.add_entrada(Entrada.crear_instancia_de_entrada_por_edad(35))
    assert str(grupo) == "Total entradas: 2, Total ingresos: 37, Entradas por tipo: {<TipoDeEntrada.BEBE: 1>: 0, <TipoDeEntrada.NIÑO: 2>: 1, <TipoDeEntrada.ADULTO: 3>: 1, <TipoDeEntrada.JUBILADO: 4>: 0}"

def test_entradas_vacias():
    grupo = Grupo_Entrada()
    assert grupo.num_entradas == 0
    assert grupo.total == 0
    assert all(cantidad == 0 for cantidad in grupo.tipos_entrada.values())

def test_multiple_entradas_mismo_tipo():
    grupo = Grupo_Entrada()
    grupo.add_entrada(Entrada.crear_instancia_de_entrada_por_edad(35))
    grupo.add_entrada(Entrada.crear_instancia_de_entrada_por_edad(35))
    grupo.add_entrada(Entrada.crear_instancia_de_entrada_por_edad(35))
    assert grupo.cantidad_entrada_por_tipo(TipoDeEntrada.ADULTO) == 3
    assert grupo.subtotal_tipo(TipoDeEntrada.ADULTO) == 69
    assert grupo.total == 69




import pytest

from tall_notes.entities.intervalos import get_valor_nota_relativa, get_valor_intervalo_entre, get_valor_intervalo, \
    get_nombre_intervalo


@pytest.mark.parametrize("valor_tonica, valor_intervalo, valor_relativa_esperada",
                         [(0, 1, 1), (0, 12, 0), (1, 12, 1), (3, 10, 1), (0, 10, 10)])
def test_get_valor_nota_relativa(valor_tonica, valor_intervalo, valor_relativa_esperada):
    valor_relativa = get_valor_nota_relativa(valor_tonica, valor_intervalo)
    assert valor_relativa_esperada == valor_relativa


@pytest.mark.parametrize("valor_tonica, valor_relativa, valor_intervalo_esperado",
                         [(0, 1, 1), (0, 0, 0), (1, 1, 0), (3, 1, 10), (0, 10, 10)])
def test_get_valor_intervalo(valor_tonica, valor_relativa, valor_intervalo_esperado):
    valor_intervalo = get_valor_intervalo_entre(valor_tonica, valor_relativa)
    assert valor_intervalo == valor_intervalo_esperado


@pytest.mark.parametrize("nombre_intervalo, valor_intervalo_esperado", [("8", 0), ("4", 5), ("5", 7)])
def test_get_valor_intervalo(nombre_intervalo, valor_intervalo_esperado):
    valor_intervalo = get_valor_intervalo(nombre_intervalo)
    assert valor_intervalo == valor_intervalo_esperado


@pytest.mark.parametrize("valor_intervalo, nombre_intervalo_esperado",
                         [(0, "8"), (5, "4"), (7, "5")])
def test_get_nombre_intervalo(valor_intervalo, nombre_intervalo_esperado):
    nombre_intervalo = get_nombre_intervalo(valor_intervalo)
    assert nombre_intervalo == nombre_intervalo_esperado

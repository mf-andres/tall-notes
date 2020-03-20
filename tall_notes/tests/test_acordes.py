import pytest

from tall_notes.entities.acordes import get_nombre_acorde, get_nombres_notas_acorde


@pytest.mark.parametrize("nombre_tonica, tipo_acorde, nombre_acorde_esperado",
                         [("DO", "M", "DOM"), ("DO", "m", "DOm"), ("DO", "dim", "DOdim")])
def test_get_nombre_acorde(nombre_tonica, tipo_acorde, nombre_acorde_esperado):
    nombre_acorde = get_nombre_acorde(nombre_tonica, tipo_acorde)
    assert nombre_acorde == nombre_acorde_esperado


@pytest.mark.parametrize("nombre_tonica, tipo_acorde, nombre_notas_esperado",
                         [("DO", "M", ["DO", "MI", "SOL"]),
                          ("DO", "m", ["DO", "RE#", "SOL"]),
                          ("DO", "dim", ["DO", "RE#", "FA#"]),
                          ("MI", "M", ["MI", "SOL#", "SI"]),
                          ("MI", "m", ["MI", "SOL", "SI"]),
                          ("MI", "dim", ["MI", "SOL", "LA#"])])
def test_get_nombres_notas_acorde(nombre_tonica, tipo_acorde, nombre_notas_esperado):
    nombre_notas = get_nombres_notas_acorde(nombre_tonica, tipo_acorde)
    assert nombre_notas == nombre_notas_esperado

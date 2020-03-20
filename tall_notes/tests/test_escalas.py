import pytest

from tall_notes.entities.escalas import get_nombre_escala, get_nombres_notas_escala, get_valores_notas_escala


def test_get_valores_notas_escala():
    valor_tonica = 0
    tipo_escala = "jonica"
    valores_notas_escala_esperados = [0, 2, 4, 5, 7, 9, 11]
    valores_notas_escala = get_valores_notas_escala(valor_tonica, tipo_escala)
    assert valores_notas_escala == valores_notas_escala_esperados
    print(f"\n valores_notas_escala = {valores_notas_escala}")


@pytest.mark.parametrize("nombre_tonica, tipo_escala, nombre_escala_esperado",
                         [("MI", "jonica", "MIjonica"), ("MI", "eolica", "MIeolica"), ("MI", "locria", "MIlocria")])
def test_get_nombre_escala(nombre_tonica, tipo_escala, nombre_escala_esperado):
    nombre_escala = get_nombre_escala(nombre_tonica, tipo_escala)
    assert nombre_escala == nombre_escala_esperado


@pytest.mark.parametrize("nombre_tonica, tipo_escala, nombres_notas_esperados",
                         [("DO", "jonica", ["DO", "RE", "MI", "FA", "SOL", "LA", "SI"]),
                          ("RE", "dorica", ["RE", "MI", "FA", "SOL", "LA", "SI", "DO"]),
                          ("MI", "frigia", ["MI", "FA", "SOL", "LA", "SI", "DO", "RE"]),
                          ("FA", "lidia", ["FA", "SOL", "LA", "SI", "DO", "RE", "MI"]),
                          ("SOL", "mixolidia", ["SOL", "LA", "SI", "DO", "RE", "MI", "FA"]),
                          ("LA", "eolica", ["LA", "SI", "DO", "RE", "MI", "FA", "SOL"]),
                          ("SI", "locria", ["SI", "DO", "RE", "MI", "FA", "SOL", "LA"])])
def test_get_nombres_notas_escala(nombre_tonica, tipo_escala, nombres_notas_esperados):
    nombre_notas = get_nombres_notas_escala(nombre_tonica, tipo_escala)
    assert nombre_notas == nombres_notas_esperados

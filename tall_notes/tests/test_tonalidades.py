import pytest

from tall_notes.entities.tonalidades import get_nombres_grados_tonalidad, get_valores_notas_grado_tonalidad, \
    get_nombre_grado_tonalidad


@pytest.mark.parametrize("posicion_nota_en_escala, valores_notas_grado_esperadas",
                         [(0, [0, 2, 4]),
                          (4, [4, 6, 1]),
                          (6, [6, 1, 3])])
def test_get_valores_notas_grado(posicion_nota_en_escala, valores_notas_grado_esperadas):
    valores_notas_escala_relativa = [0, 1, 2, 3, 4, 5, 6]
    valores_notas_grado = get_valores_notas_grado_tonalidad(posicion_nota_en_escala, valores_notas_escala_relativa)
    assert valores_notas_grado == valores_notas_grado_esperadas


@pytest.mark.parametrize("posicion_nota_en_escala, nombre_grado_tonalidad_esperado",
                         [(0, "DOM"),
                          (4, "SOLM"),
                          (5, "LAm"),
                          (6, "SIdim")])
def test_get_nombre_grado_tonalidad(posicion_nota_en_escala, nombre_grado_tonalidad_esperado):
    valores_notas_escala_relativa = [0, 2, 4, 5, 7, 9, 11]
    nombre_grado_tonalidad = get_nombre_grado_tonalidad(posicion_nota_en_escala, valores_notas_escala_relativa)
    assert nombre_grado_tonalidad == nombre_grado_tonalidad_esperado



@pytest.mark.parametrize("nombre_tonica, tipo_tonalidad, nombres_grados_tonalidad_esperados",
                         [("DO", "jonica", ["DOM", "REm", "MIm", "FAM", "SOLM", "LAm", "SIdim"]),
                          ("RE", "dorica", ["REm", "MIm", "FAM", "SOLM", "LAm", "SIdim", "DOM"]),
                          ("MI", "frigia", ["MIm", "FAM", "SOLM", "LAm", "SIdim", "DOM", "REm"]),
                          ("FA", "lidia", ["FAM", "SOLM", "LAm", "SIdim", "DOM", "REm", "MIm"]),
                          ("SOL", "mixolidia", ["SOLM", "LAm", "SIdim", "DOM", "REm", "MIm", "FAM"]),
                          ("LA", "eolica", ["LAm", "SIdim", "DOM", "REm", "MIm", "FAM", "SOLM"]),
                          ("SI", "locria", ["SIdim", "DOM", "REm", "MIm", "FAM", "SOLM", "LAm"])])
def test_get_nombres_grados_tonalidad(nombre_tonica, tipo_tonalidad, nombres_grados_tonalidad_esperados):
    nombres_grados_tonalidad = get_nombres_grados_tonalidad(nombre_tonica, tipo_tonalidad)
    assert nombres_grados_tonalidad == nombres_grados_tonalidad_esperados

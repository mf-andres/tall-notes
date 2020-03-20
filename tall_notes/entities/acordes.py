import numpy as np

from tall_notes.entities.intervalos import get_valor_intervalo, get_valor_nota_relativa, get_nombre_intervalo, \
    get_valor_intervalo_entre
from tall_notes.entities.notas import get_valor_nota, get_nombre_nota

# tipo acorde : patron_acorde
acordes = {
    "M": ["3M", "5"],
    "m": ["3m", "5"],
    "dim": ["3m", "5m"]
}


# devuelve un array con los valores de las notas a partir del valor de la tonica y el tipo de acorde
def get_valores_notas_acorde(valor_tonica, tipo_acorde):
    patron_acorde = acordes[tipo_acorde]
    valores_notas = list()
    valores_notas.append(valor_tonica)
    for nombre_intervalo in patron_acorde:
        valor_intervalo = get_valor_intervalo(nombre_intervalo)
        valor_nota = get_valor_nota_relativa(valor_tonica, valor_intervalo)
        valores_notas.append(valor_nota)
    return valores_notas


# devuelve un array con nombres de intervalos a partir de un tipo de acorde
def get_patron_acorde(tipo_acorde):
    return acordes[tipo_acorde]


# devuelve el tipo de acorde a partir de un array de valores de notas
def get_tipo_acorde(valores_notas):
    if len(valores_notas) == 3:
        nombre_intervalo_1 = get_nombre_intervalo(
            get_valor_intervalo_entre(valores_notas[0], valores_notas[1]))  # TODO get_nombre_intervalo_entre
        nombre_intervalo_2 = get_nombre_intervalo(
            get_valor_intervalo_entre(valores_notas[0], valores_notas[2]))
        patron_a_identificar = [nombre_intervalo_1, nombre_intervalo_2]
        for i, patron_conocido in enumerate(list(acordes.values())):
            if np.array_equal(patron_a_identificar, patron_conocido):
                return list(acordes.keys())[i]
    else:
        raise ValueError("valores_notas sigue un patrón no conocido")


def get_nombre_acorde(nombre_tonica, tipo_acorde):
    nombre_acorde = nombre_tonica + tipo_acorde
    return nombre_acorde


def get_nombres_notas_acorde(nombre_tonica, tipo_acorde):
    valor_tonica = get_valor_nota(nombre_tonica)
    valores_notas = get_valores_notas_acorde(valor_tonica, tipo_acorde)
    nombres_notas = [get_nombre_nota(valor_nota) for valor_nota in valores_notas]
    return nombres_notas

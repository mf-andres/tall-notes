import numpy as np
from tall_notes.entities import notas, intervalos
from tall_notes.entities.notas import get_nombre_nota, get_valor_nota

# tipo_escala: patron_escala
escalas = {
    "jonica": ["2M", "3M", "4", "5", "6M", "7M"],
    "dorica": ["2M", "3m", "4", "5", "6M", "7m"],
    "frigia": ["2m", "3m", "4", "5", "6m", "7m"],
    "lidia": ["2M", "3M", "5m", "5", "6M", "7M"],
    "mixolidia": ["2M", "3M", "4", "5", "6M", "7m"],
    "eolica": ["2M", "3m", "4", "5", "6m", "7m"],
    "locria": ["2m", "3m", "4", "5m", "6m", "7m"],
}


# obtiene un array de valores de notas a partir del valor de la tonica y el tipo de escala
def get_valores_notas_escala(valor_tonica, tipo_escala):  # TODO same as acordes
    patron_escala = escalas[tipo_escala]
    valores_notas = list()
    valores_notas.append(valor_tonica)
    for nombre_intevalo in patron_escala:
        valor_intervalo = intervalos.get_valor_intervalo(nombre_intevalo)
        valor_nota = intervalos.get_valor_nota_relativa(valor_tonica, valor_intervalo)
        valores_notas.append(valor_nota)
    return valores_notas


# obtiene un array con nombres de intervalos a partir de un tipo de escala
def get_patron_escala(escala):
    return escalas[escala]


# TODO not in use
# # devuelve el tipo de escala a partir de un array de valores de notas
# def get_tipo_escala(valores_notas):
#     if len(valores_notas) == 7:
#         patron_1 = list()
#         for i in range(1, 7):
#             nombre_intervalo = intervalos.get_nombre_intervalo(
#                 intervalos.get_valor_intervalo_entre(valores_notas[0], valores_notas[i]))  # TODO function
#             patron_1.append(nombre_intervalo)
#         i = 0
#         for patron_2 in list(escalas.values()):
#             if np.array_equal(patron_1, patron_2):
#                 return list(escalas.keys())[i]
#             i += 1
#         raise ValueError("valores_notas sigue un patrón no conocido")
#     else:
#         raise ValueError("valores_notas debe contener 7 notas")


def get_nombre_escala(nombre_tonica, tipo_escala):  # TODO same as nombre acorde
    nombre_escala = nombre_tonica + tipo_escala
    return nombre_escala


def get_nombres_notas_escala(nombre_tonica, tipo_escala):
    valor_tonica = get_valor_nota(nombre_tonica)
    valores_notas = get_valores_notas_escala(valor_tonica, tipo_escala)
    nombres_notas = [get_nombre_nota(valor_nota) for valor_nota in valores_notas]  # TODO same as nombre acorde
    return nombres_notas
from tall_notes.entities.notas import get_nombre_nota, get_valor_nota
from tall_notes.entities.acordes import get_tipo_acorde, get_nombre_acorde, get_valores_notas_acorde
from tall_notes.entities.escalas import get_nombre_escala, get_patron_escala, get_valores_notas_escala


# obtiene un array de arrays (grados) con los valores de las notas de cada uno de los grados de la tonalidad
def get_valores_notas_grados_tonalidad(valor_tonica, tipo_tonalidad):
    valores_notas_escala_relativa = get_valores_notas_acorde(valor_tonica, tipo_tonalidad)
    grados_tonalidad = list()
    for i in range(len(valores_notas_escala_relativa)):
        grado = list()
        grado.append(valores_notas_escala_relativa[i])
        n = i
        for j in range(2):
            n = (n + 2) % len(valores_notas_escala_relativa)
            grado.append(valores_notas_escala_relativa[n])
        grados_tonalidad.append(grado)
    return grados_tonalidad


# obtiene un array con los intervalos de cada una de las tonicas de los grados respecto a la tonica del grado fundamental
def get_nombres_intervalos(tipo_tonalidad):
    return get_patron_escala(tipo_tonalidad)


# obtiene los nombres de las tonicas de cada grado
def get_nombres_tonicas(tonica, tonalidad):
    valores_tonicas = get_valores_notas_acorde(tonica, tonalidad)
    nombres_tonicas = [get_nombre_nota(valor_tonica) for valor_tonica in valores_tonicas]
    return nombres_tonicas


# obtiene los tipos de acorde a partir del tipo de tonalidad
def get_tipos_acorde(tipo_tonalidad):
    valores_notas_grados_tonalidad = get_valores_notas_grado_tonalidad(0, tipo_tonalidad)
    tipos_acordes = list()
    for grado in valores_notas_grados_tonalidad:
        tipos_acordes.append(get_tipo_acorde(grado))
    return tipos_acordes


def get_nombre_tonalidad(nombre_tonica, tipo_tonalidad):
    return get_nombre_escala(nombre_tonica, tipo_tonalidad)


def get_valores_notas_grado_tonalidad(posicion_valor_tonica_en_escala, valores_notas_escala):
    valor_tonica = valores_notas_escala[posicion_valor_tonica_en_escala]
    valores_notas_acorde = [valor_tonica]
    posicion_siguiente_nota_en_escala = posicion_valor_tonica_en_escala
    for j in range(2):
        posicion_siguiente_nota_en_escala = (posicion_siguiente_nota_en_escala + 2) % len(valores_notas_escala)
        valor_siguiente_nota = valores_notas_escala[posicion_siguiente_nota_en_escala]
        valores_notas_acorde.append(valor_siguiente_nota)
    return valores_notas_acorde


def get_nombre_grado_tonalidad(posicion_nota_en_escala, valores_notas_escala_relativa):  # TODO test
    valores_notas_acorde_grado = get_valores_notas_grado_tonalidad(posicion_nota_en_escala, valores_notas_escala_relativa)
    tipo_acorde_grado = get_tipo_acorde(valores_notas_acorde_grado)
    valor_tonica_grado = valores_notas_acorde_grado[0]
    nombre_tonica_grado = get_nombre_nota(valor_tonica_grado)
    nombre_grado_tonalidad = get_nombre_acorde(nombre_tonica_grado, tipo_acorde_grado)
    return nombre_grado_tonalidad


def get_nombres_grados_tonalidad(nombre_tonica, tipo_tonalidad):
    valor_tonica = get_valor_nota(nombre_tonica)
    valores_notas_escala_relativa = get_valores_notas_escala(valor_tonica, tipo_tonalidad)
    nombres_grados_tonalidad = list()
    for posicion_nota_en_escala in range(len(valores_notas_escala_relativa)):
        nombre_grado = get_nombre_grado_tonalidad(posicion_nota_en_escala, valores_notas_escala_relativa)
        nombres_grados_tonalidad.append(nombre_grado)
    return nombres_grados_tonalidad

# def get_nombres_grados_tonalidad(nombre_tonica, tipo_tonalidad):
#     valor_tonica = get_valor_nota(nombre_tonica)
#     valores_notas_grados_tonalidad = get_valores_notas_grados_tonalidad(valor_tonica, tipo_tonalidad)
#     nombres_grados_tonalidad = list()
#     for grado in valores_notas_grados_tonalidad:
#         tipo_acorde_grado = get_tipo_acorde(grado)
#         valor_tonica_grado = grado[0]
#         nombre_tonica_grado = get_nombre_nota(valor_tonica_grado)
#         nombre_grado = get_nombre_acorde(nombre_tonica_grado, tipo_acorde_grado)
#         nombres_grados_tonalidad.append(nombre_grado)
#     return nombres_grados_tonalidad

notas = {
    "DO": 0,
    "DO#": 1,
    "RE": 2,
    "RE#": 3,
    "MI": 4,
    "FA": 5,
    "FA#": 6,
    "SOL": 7,
    "SOL#": 8,
    "LA": 9,
    "LA#": 10,
    "SI": 11
}


def get_valor_nota(nombre_nota):
    return notas[nombre_nota]


def get_nombre_nota(valor_nota):
    return list(notas.keys())[valor_nota]


def formatea_nombre_notas(valores_nota):
    nombre_notas = str()
    for nota in valores_nota:
        nombre_nota = get_nombre_nota(nota)
        nombre_notas = nombre_notas + ", " + str(nombre_nota)
    nombre_notas = "(" + nombre_notas[2:] + ")"
    return nombre_notas

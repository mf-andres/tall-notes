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

def getValor(nombre):
    return notas[nombre]

def getNombre(valor):
    return list(notas.keys())[valor]

def nombreNotas(notas):
    nombreNotas = str()
    for nota in notas:
        nombreNota = getNombre(nota)
        nombreNotas = nombreNotas + ", " + str(nombreNota)
    nombreNotas = "(" + nombreNotas[2:] + ")"
    return nombreNotas
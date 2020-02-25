intervalos = {
    "2m": 1,
    "2M": 2,
    "3m": 3,
    "3M": 4,
    "4": 5,
    "5m": 6,
    "5": 7,
    "6m": 8,
    "6M": 9,
    "7m": 10,
    "7M": 11,
    "8": 12
}

#devuelve el valor de la nota
def getNota(tonica, intervalo):
    return (tonica + intervalo) % 12

#devuelve el valor del intervalo
def getIntervalo(tonica, relativa):
    return relativa - tonica

def getValorIntervalo(nombreIntervalo):
    return intervalos[nombreIntervalo]

def getNombreIntervalo(valorIntervalo):
    return list(intervalos.keys())[valorIntervalo-1]
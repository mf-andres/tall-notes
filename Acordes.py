import numpy as np
import Intervalos
import Notas

acordes = {
    "M": ["3M", "5"],
    "m": ["3m", "5"],
    "dim": ["3m", "5m"]
}

#devuelve un array con los valores de las notas a partir del valor de la tonica y el tipo de acorde
def getNotas(tonica, acorde):
    patron = acordes[acorde]
    notas = list()
    notas.append(tonica)
    for nombreIntervalo in patron:
        intervalo = Intervalos.getValorIntervalo(nombreIntervalo)
        nota = Intervalos.getNota(tonica, intervalo)
        notas.append(nota)
    return notas

#devuelve un array con nombres de intervalos a partir de un tipo de acorde
def getIntervalos(acorde):
    return acordes[acorde]

#devuelve el tipo de acorde a partir de un array de valores de notas
def getAcorde(notas):
    if len(notas) == 3:
        nombreIntervalo1 = Intervalos.getNombreIntervalo(Intervalos.getIntervalo(notas[0],notas[1]))
        nombreIntervalo2 = Intervalos.getNombreIntervalo(Intervalos.getIntervalo(notas[0],notas[2]))
        patron1 = [nombreIntervalo1, nombreIntervalo2]
        i = 0
        for patron2 in list(acordes.values()):
            if np.array_equal(patron1, patron2):
                return list(acordes.keys())[i]
            i += 1
    #TODO lanzar excepcion si no hay resultado

def getNombreAcorde(notas):
    nombre = str(Notas.getNombre(notas[0]))
    nombre = nombre + str(getAcorde(notas))
    return nombre

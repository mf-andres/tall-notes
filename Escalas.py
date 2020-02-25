import numpy as np
import Intervalos
import Notas

escalas = {
    "jonica": ["2M", "3M", "4", "5", "6M", "7M"],
    "dorica": ["2M", "3m", "4", "5", "6M", "7m"],
    "frigio": ["2m", "3m", "4", "5", "6m", "7m"],
    "lidio": ["2M", "3M", "5m", "5", "6M", "7M"],
    "mixolidio": ["2M", "3M", "4", "5", "6M", "7m"],
    "eolico": ["2M", "3m", "4", "5", "6m", "7m"],
    "locrio": ["2m", "3m", "4", "5m", "6m", "7m"],
}

#obtiene un array de valores de notas a partir del valor de la tonica y el tipo de escala
def getNotas(tonica, escala):
    patron = escalas[escala]
    notas = list()
    notas.append(tonica)
    for nombreIntervalo in patron:
        intervalo = Intervalos.getValorIntervalo(nombreIntervalo)
        nota = Intervalos.getNota(tonica, intervalo)
        notas.append(nota)
    return notas

#obtiene un array con nombres de intervalos a partir de un tipo de escala
def getIntervalos(escala):
    return escalas[escala]

#devuelve el tipo de escala a partir de un array de valores de notas
def getEscala(notas):
    if len(notas) == 7:
        patron1 = list()
        for i in range(1,7):
            nombreIntervalo = Intervalos.getNombreIntervalo(Intervalos.getIntervalo(notas[0], notas[i]))
            patron1.append(nombreIntervalo)
        i = 0
        for patron2 in list(escalas.values()):
            if np.array_equal(patron1, patron2):
                return list(escalas.keys())[i]
            i += 1
    #TODO excepcion si no aparece resultado

def getNombreEscala(notas):
    nombreEscala = str(Notas.getNombre(notas[0]))
    nombreEscala = nombreEscala + str(getEscala(notas))
    return nombreEscala
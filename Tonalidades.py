import Acordes
import Escalas

#las tonalidades tendrán el mismo tipaje que las escalas

#obtiene un array de arrays (grados) con los valores de las notas de cada uno de los grados de la tonalidad
def getGrados(tonica, tonalidad):
    escala = Escalas.getNotas(tonica, tonalidad)
    grados = list()
    for i in range(len(escala)):
        grado = list()
        grado.append(escala[i])
        n = i
        for j in range(2):
            n = (n + 2) % len(escala)
            grado.append(escala[n])
        grados.append(grado)
    return grados

#obtiene un array con los intervalos de cada una de las tonicas de los grados respecto a la tonica del grado fundamental
def getIntervalos(tonalidad):
    return Escalas.getIntervalos()

#obtiene los valores de las tonicas de cada grado
def getTonicas(tonica, tonalidad):
    return Escalas.getNotas(tonica, tonalidad)

#obtiene los tipos de acorde a partir del tipo de tonalidad
def getAcordes(tonalidad):
    grados = getGrados(0, tonalidad)
    acordes = list()
    for grado in grados:
        acordes.append(Acordes.getAcorde(grado))
    return acordes

def getNombreGrados(tonica, tonalidad):
    grados = getGrados(tonica, tonalidad)
    nombresAcordes = str()
    for grado in grados:
        nombreAcorde = Acordes.getNombreAcorde(grado)
        nombresAcordes = nombresAcordes + ", " + nombreAcorde
    nombresAcordes = "(" + nombresAcordes[2:] + ")"
    return nombresAcordes
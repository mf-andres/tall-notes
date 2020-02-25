import Notas
import Acordes
import Escalas
import Tonalidades

import json

if __name__ == '__main__':

    tall_notes_dict = dict()
    file = open("TallNotes.txt", "wt")

    # obtencion acordes
    chords = dict()
    file.write("### Acordes\n")
    file.write("\n")

    for nota in Notas.notas:
        tonica = Notas.getValor(nota)
        for acorde in list(Acordes.acordes.keys()):
            notas = Acordes.getNotas(tonica, acorde)
            nombreAcorde = Acordes.getNombreAcorde(notas)
            nombreNotas = Notas.nombreNotas(notas)
            chords[nombreAcorde] = nombreNotas[1:-1].split(', ')
            file.write(str(nombreAcorde) + " " + str(nombreNotas) + "\n")
        file.write("\n")

    # obtencion escalas
    scales = dict()
    file.write("\n")
    file.write("### Escalas")
    file.write("\n")

    for nota in Notas.notas:
        tonica = Notas.getValor(nota)
        for escala in list(Escalas.escalas.keys()):
            notas = Escalas.getNotas(tonica, escala)
            nombreEscala = Escalas.getNombreEscala(notas)
            nombreNotas = Notas.nombreNotas(notas)
            scales[nombreEscala] = nombreNotas[1:-1].split(', ')
            file.write(str(nombreEscala + " " + str(nombreNotas)) + "\n")
        file.write("\n")

    # obtencion tonalidades
    tonalities = dict()
    file.write("\n")
    file.write("### Tonalidades\n")
    file.write("\n")

    for nota in Notas.notas:
        tonica = Notas.getValor(nota)
        for escala in list(Escalas.escalas.keys()):
            nombreGrados = Tonalidades.getNombreGrados(tonica, escala)
            tonalities[nota + escala] = nombreGrados[1:-1].split(', ')
            file.write(nota + escala + " " + str(nombreGrados) + "\n")
        file.write("\n")

    file.close()

    tall_notes_dict['chords'] = chords
    tall_notes_dict['scales'] = scales
    tall_notes_dict['tonalities'] = tonalities
    with open('TallNotes.json', 'w') as json_file:
        json.dump(tall_notes_dict, json_file, sort_keys=False, indent=4, separators=(',', ': '))

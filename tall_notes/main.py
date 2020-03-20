from tall_notes.entities import notas, tonalidades, acordes, escalas

import json


def get_diccionario_con_todos_los_acordes():
    diccionario_de_acordes = dict()
    for nombre_nota in notas.notas:
        for tipo_acorde in acordes.acordes:
            nombre_acorde = acordes.get_nombre_acorde(nombre_nota, tipo_acorde)
            nombres_notas_acorde = acordes.get_nombres_notas_acorde(nombre_nota, tipo_acorde)
            diccionario_de_acordes[nombre_acorde] = nombres_notas_acorde
    return diccionario_de_acordes


def get_diccionario_con_todas_las_escalas():
    diccionario_de_escalas = dict()
    for nombre_nota in notas.notas:
        for tipo_escala in escalas.escalas:
            nombre_escala = escalas.get_nombre_escala(nombre_nota, tipo_escala)
            nombre_notas_escala = escalas.get_nombres_notas_escala(nombre_nota, tipo_escala)
            diccionario_de_escalas[nombre_escala] = nombre_notas_escala
    return diccionario_de_escalas


def get_diccionario_con_todas_las_tonalidades():
    diccionario_de_tonalidades = dict()
    for nombre_nota in notas.notas:
        for tipo_escala in escalas.escalas:
            nombre_tonalidad = tonalidades.get_nombre_tonalidad(nombre_nota, tipo_escala)
            nombre_grados_tonalidad = tonalidades.get_nombres_grados_tonalidad(nombre_nota, tipo_escala)
            diccionario_de_tonalidades[nombre_tonalidad] = nombre_grados_tonalidad
    return diccionario_de_tonalidades


def imprimir_tall_notes_como_json(diccionario_tall_notes):
    # imprimir en formato json
    with open('./assets/tall_notes.json', 'w') as json_file:
        json.dump(diccionario_tall_notes, json_file, sort_keys=False, indent=4, separators=(',', ': '))


def imprimir_tall_notes_como_txt(diccionario_tall_notes):
    with open("./assets/tall_notes.txt", "wt") as file:
        file.write("### Acordes\n")
        for acorde in diccionario_tall_notes["chords"]:
            file.write(f"{str(acorde)} {str(diccionario_tall_notes['chords'][acorde])}\n")
        file.write("\n")

        file.write("\n")
        file.write("### Escalas\n")
        for escala in diccionario_tall_notes["scales"]:
            file.write(f"{str(escala)} {str(diccionario_tall_notes['scales'][escala])}\n")
        file.write("\n")

        file.write("\n")
        file.write("### Tonalidades\n")
        for tonalidad in diccionario_tall_notes["tonalities"]:
            file.write(f"{str(tonalidad)} {str(diccionario_tall_notes['tonalities'][tonalidad])}\n")
        file.write("\n")


if __name__ == '__main__':
    diccionario_tall_notes = dict()
    diccionario_tall_notes['chords'] = get_diccionario_con_todos_los_acordes()
    diccionario_tall_notes['scales'] = get_diccionario_con_todas_las_escalas()
    diccionario_tall_notes['tonalities'] = get_diccionario_con_todas_las_tonalidades()

    imprimir_tall_notes_como_json(diccionario_tall_notes)
    imprimir_tall_notes_como_txt(diccionario_tall_notes)

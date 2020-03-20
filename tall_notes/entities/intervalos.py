intervalos = {
    "8": 0,
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
}


def get_valor_nota_relativa(valor_tonica, valor_intervalo):
    return (valor_tonica + valor_intervalo) % 12


def get_valor_intervalo_entre(valor_tonica, valor_relativa):
    return (valor_relativa - valor_tonica) % 12


def get_valor_intervalo(nombre_intervalo):
    return intervalos[nombre_intervalo]


def get_nombre_intervalo(valor_intervalo):
    return list(intervalos.keys())[valor_intervalo]

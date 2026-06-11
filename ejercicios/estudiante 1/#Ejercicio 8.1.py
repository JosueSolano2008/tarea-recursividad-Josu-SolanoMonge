def detectar_valles(lista, resultado=[]):
    if len(lista) < 3:
        return resultado

    if lista[0] > lista[1] and lista[2] > lista[1]:
        return detectar_valles(lista[1:], resultado + [[lista[0], lista[1], lista[2]]])

    return detectar_valles(lista[1:], resultado)

print(detectar_valles([5, 1, 6, 3, 8, 2, 7]))
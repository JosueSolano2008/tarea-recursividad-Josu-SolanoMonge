#Ejercicio 10
#Cola
def comprimir_repetidos(lista, resultado=[], actual=[]):
    if len(lista) == 0:
        return resultado + [actual] if actual else resultado
    if actual == [] or lista[0] == actual[0]:
        return comprimir_repetidos(lista[1:], resultado, [lista[0], actual[1] + 1] if actual else [lista[0], 1])
    return comprimir_repetidos(lista[1:], resultado + [actual], [lista[0], 1])

print(comprimir_repetidos([1, 1, 1, 2, 2, 3, 1, 1]))
print(comprimir_repetidos([5, 5, 5, 5]))
print(comprimir_repetidos([]))
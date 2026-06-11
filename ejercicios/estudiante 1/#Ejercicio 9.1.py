#Ejercicio 9 
#Cola
def sublistas_ascendentes(lista, resultado=[], actual=[]):
    if len(lista) == 0:
        return resultado + [actual] if actual else resultado
    if actual == [] or lista[0] > actual[-1]:
        return sublistas_ascendentes(lista[1:], resultado, actual + [lista[0]])
    return sublistas_ascendentes(lista[1:], resultado + [actual], [lista[0]])

print(sublistas_ascendentes([1, 2, 3, 1, 4, 5, 2]))
print(sublistas_ascendentes([5, 4, 3, 2]))
print(sublistas_ascendentes([2, 2, 3, 1, 2]))
print(sublistas_ascendentes([]))
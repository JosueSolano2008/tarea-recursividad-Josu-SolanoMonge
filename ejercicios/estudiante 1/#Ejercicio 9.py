#Ejercicio 9
#Pila
def sublistas_ascendentes(lista):
    if len(lista) == 0:
        return []
    resultado = sublistas_ascendentes(lista[1:])
    if resultado == []:
        return [[lista[0]]]
    if lista[0] < resultado[0][0]:
        return [[lista[0]] + resultado[0]] + resultado[1:]
    return [[lista[0]]] + resultado

print(sublistas_ascendentes([1, 2, 3, 1, 4, 5, 2]))
print(sublistas_ascendentes([5, 4, 3, 2]))
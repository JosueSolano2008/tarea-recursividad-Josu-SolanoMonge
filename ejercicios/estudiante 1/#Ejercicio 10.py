#Ejercicio 10
#Pila
def comprimir_repetidos(lista):
    if len(lista) == 0:
        return []
    resultado = comprimir_repetidos(lista[1:])
    if resultado != [] and lista[0] == resultado[0][0]:
        return [[resultado[0][0], resultado[0][1] + 1]] + resultado[1:]
    return [[lista[0], 1]] + resultado

print(comprimir_repetidos([1, 1, 1, 2, 2, 3, 1, 1]))
print(comprimir_repetidos([5, 5, 5, 5]))
print(comprimir_repetidos([1, 2, 3, 4]))
print(comprimir_repetidos([]))
#Ejercicio 8
#Pila
def detectar_valles(lista):
    if len(lista)<3:
        return []
    
    resto=detectar_valles(lista[1:])

    if lista[0] > lista[1] and lista [2] > lista[1]:
        return [[lista[0],lista[1],lista[2]]] + resto
    
    return resto

print(detectar_valles([5, 1, 6, 3, 8, 2, 7]))
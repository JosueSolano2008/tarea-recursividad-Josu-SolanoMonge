#Ejercicio 6
#Pila
def contar_bloques_iguales(lista):
    if lista == []:
        return 0
    if len(lista) <= 1:
        return 1
    if lista[0] != lista [1]:
        return contar_bloques_iguales(lista[1:])+(1)
    return contar_bloques_iguales(lista[1:])+(0)

print(contar_bloques_iguales([]))
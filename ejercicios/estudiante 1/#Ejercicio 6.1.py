#Ejercicio 6
#Cola
def contar_bloques_iguales(lista):
    if len(lista) == 0:
            return 0
    def helper (lista,acum=1):
        if len(lista) <= 1:
             return acum
        anterior=lista[0]
        siguiente=lista[1]
        if anterior != siguiente:
             return helper (lista[1:], acum + 1)
        else:
            return helper (lista[1:],acum)

    return helper(lista)

print(contar_bloques_iguales([1, 1, 2, 2, 2, 3, 1, 1]))
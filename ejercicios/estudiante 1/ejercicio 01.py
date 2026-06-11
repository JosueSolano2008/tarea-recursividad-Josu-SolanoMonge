#Ejercicio 1
#Pila:
def sumar_digitosP(n):
    if n == 0:
        return 0
    return sumar_digitosP(n//10)+(n%10)

#Ejercicio 1
#Cola:
def sumar_digitosC(n, acum=0):
    if n==0:
        return acum
    return sumar_digitosC( n // 10 , acum + ( n % 10 ))
#Ejercicio 7
#Pila
def separar_por_paridad(num):
    if  num == 0:
        return 0 , 0
    
    pares, impares = separar_por_paridad(num//10)
    digito = num % 10      

    if digito % 2 == 0:
        return pares * 10 + digito, impares
    else:
        return pares, impares * 10 + digito

print(separar_por_paridad(80231))
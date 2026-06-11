#Ejercicio 4
#Pila
def contar_numeros(num):
    if num == 0:
        return 0
    return contar_numeros(num//10)+1

def invertir_numero(num):
    if num == 0:
        return 0
    return invertir_numero(num//10)+((num%10)*10**(contar_numeros(num)-1))

print(invertir_numero(1234))
#Ejercicio 5
#Cola
def contar_digitos(num,acum=0):
    if num ==0:
        return acum
    return contar_digitos(num//10 , acum+1)

def eliminar_impares(num):
    def helper(num, acum=0):
        if num == 0:
            return acum
        digito = num % 10
        if digito % 2 == 0:
            return helper(num // 10, acum + digito * 10**contar_digitos(acum))
        return helper(num // 10, acum)
    return helper(num)

print(eliminar_impares(80246))
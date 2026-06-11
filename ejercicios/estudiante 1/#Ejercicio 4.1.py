#Ejercicio 4
#Cola
def contar_digitos(num,acum=0):
    if num ==0:
        return acum
    return contar_digitos(num//10 , acum+1)

def invertir_numero(num, acum=0):
    digitos = contar_digitos(num)
    def helper (num, acum=0, pos=None):
        if pos is None:
            pos = digitos - 1
        if num == 0:
            return acum
        return helper (num//10, acum + (num%10)* 10**pos,pos-1)
    return helper(num)

print(invertir_numero(900))
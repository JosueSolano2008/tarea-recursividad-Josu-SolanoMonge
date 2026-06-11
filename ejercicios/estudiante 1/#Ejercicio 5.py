def eliminar_impares(num):
    if num ==0:
        return 0
    resto = eliminar_impares(num//10)
    if num%2==0:
        return resto * 10 + (num%10)
    return resto
    
print(eliminar_impares(1234567890))
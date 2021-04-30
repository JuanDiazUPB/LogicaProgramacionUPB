n = int(input('Introduzca un número de 4 dígitos: '))
reverso = 0
while n > 0:
    residuo = n % 10
    reverso = (reverso * 10) + residuo
    n = n // 10
print('\nEl reverso del numero es:', reverso)

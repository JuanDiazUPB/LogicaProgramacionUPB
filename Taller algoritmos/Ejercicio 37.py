n1 = int(input('Introduzca el primer número: '))
n2 = int(input('Introduzca el segundo número: '))
n3 = int(input('Introduzca el tercer número: '))
if n1 < n2 < n3:
    print('\nLos números están incrementando')
elif n1 > n2 > n3:
    print('\nLos números están disminuyendo')
else:
    print('\nLos números no están aumentando ni disminuyendo')

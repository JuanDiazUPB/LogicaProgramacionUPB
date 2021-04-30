n1 = int(input('Introduzca el primer número: '))
n2 = int(input('Introduzca el segundo número: '))
if n2 > n1:
    print()
    suma = []
    for x in range(n1, n2 + 1):
        suma.append(x)
        print(x)
    print(f'\nLa suma de los valores es {sum(suma)}')
else:
    print('\nn1 es mayor que n2...')

n1 = int(input('Introduzca el primer número: '))
n2 = int(input('Introduzca el segundo número: '))
if n2 > n1:
    print()
    for x in range(n1, n2 + 1):
        print(x)
else:
    print('\nn1 es mayor que n2...')

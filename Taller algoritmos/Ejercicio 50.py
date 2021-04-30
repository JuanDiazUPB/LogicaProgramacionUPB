prompar = []
promimpar = []
while True:
    n = int(input('Introduzca un número (0 para detener el programa): '))
    if n == 0:
        break
    if n % 2 == 0:
        prompar.append(n)
    elif n % 2 != 0:
        promimpar.append(n)
print(f'Promedio números pares: {sum(prompar) / len(prompar)}')
print(f'Promedio números impares: {sum(promimpar) / len(promimpar)}')

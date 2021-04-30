men100 = []
may100 = []
while True:
    n = int(input('Introduzca un número (0 para detener el programa): '))
    if n == 0:
        break
    if n > 100:
        may100.append(n)
    else:
        men100.append(n)
print(f'\nLos valores mayores a 100 fueron: {may100}')
print(f'Los valores menores a 100 fueron: {men100}')

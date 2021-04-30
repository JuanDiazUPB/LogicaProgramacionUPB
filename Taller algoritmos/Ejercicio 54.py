pares = []
impares = []
cinco = []
i = 0
while True:
    n = int(input('Introduzca un número positivo (0 para detener el programa): '))
    if n == 0:
        break
    if n < 0:
        print('El número es negativo...')
    if n == 5:
        i += 1
        cinco.append(n)
        if len(cinco) == 20:
            break
    if n % 2 == 0:
        i += 1
        pares.append(n)
        if len(pares) == 10:
            break
    elif n % 2 != 0:
        i += 1
        impares.append(n)
print(f'Se leyeron en total {i} números. {len(pares)} fueron pares, {len(impares)} fueron impares, y 5 se escribió un '
      f'total de {len(cinco)} veces.')

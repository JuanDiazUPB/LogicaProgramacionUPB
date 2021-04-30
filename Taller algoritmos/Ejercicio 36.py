n = str(input('Introduzca un número menor a 100.000: '))
if len(n) >= 6:
    print('El número es mayor o igual a 100.000...')
else:
    print(f'El número introducido tiene {len(n)} dígitos')

while True:
    try:
        n = int(input('Introduzca un número entero positivo: '))
        if n < 0:
            print('El número es negativo...')
        else:
            print(f'El número es {n}')
            break
    except:
        print('El valor es inválido...')

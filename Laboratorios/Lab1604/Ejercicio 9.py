numero = str(input('Digite su cédula de ciudadanía: '))


def cedula(n):
    cantidad = len(n)
    if 7 <= cantidad <= 10:
        valido = True
        print('\nLa cédula es válida\n')
    else:
        valido = False
        print('\nLa cédula es inválida\n')
    print(f'La cédula introducida tiene {cantidad} dígitos')
    print(f'El valor booleano es: {valido}')


cedula(numero)

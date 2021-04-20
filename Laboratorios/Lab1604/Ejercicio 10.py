cadena = str(input("Introduzca una palabra: "))


def contador_palabra(cadena):
    lista = cadena.split()
    ultima_palabra = lista[-1]
    print(f'Letras en palabra: {len(ultima_palabra)}')


contador_palabra(cadena)

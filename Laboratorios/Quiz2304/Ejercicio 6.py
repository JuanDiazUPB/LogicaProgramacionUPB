palabra = str(input('Introduzca una palabra: '))
if palabra == palabra[::-1]:
    print("La palabra ingresada es un palíndromo")
else:
    print("La palabra ingresada NO es un palíndromo")

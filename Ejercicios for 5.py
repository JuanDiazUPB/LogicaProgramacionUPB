print('Ejercicio 5: Solicitar al usuario que ingrese una frase y luego imprimir un listado de las vocales que aparecen en esa frase (sin repetirlas).')
frase = str(input('Escriba una frase: '))
print('Vocales en frase:')
for x in 'aeiou':
    if x in frase:
        print(x)
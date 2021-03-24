print('Ejercicio 8: Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los años en ese rango, que sean bisiestos y múltiplos de 10.')
anioInicio = int(input("Año inicial: "))
anioFin = int(input("Año final: "))
for anio in range(anioInicio, anioFin+1):
    if not anio % 10 == 0:
        continue
    if not anio % 4 == 0:
        continue
    if anio % 100 != 0 or anio % 400 == 0:
        print(anio)

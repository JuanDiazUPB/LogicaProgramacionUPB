def sumaDigitos(numero):
    suma = 0
    while numero != 0:
        digito = numero % 10
        suma = suma + digito
        numero = numero // 10
    return suma


cantidad = 0
mayor = -1
numero = int(input("Introduzca un número positivo (digite un negativo para detener el proceso): "))
# Instrucciones más claras
while numero >= 0:
    suma = sumaDigitos(numero)
    if suma > mayor:
        mayor = suma
        n_mayorsuma = numero
    if suma < 10:
        cantidad += 1
    numero = int(input("Introduzca un número positivo (digite un negativo para detener el proceso): "))
# Formato más fácil de leer
print(f"\nSumatoria de dígitos del número mas largo ({n_mayorsuma}): {mayor}")
print(f"Cantidad de números con sumatoria menor a 10: {cantidad}")

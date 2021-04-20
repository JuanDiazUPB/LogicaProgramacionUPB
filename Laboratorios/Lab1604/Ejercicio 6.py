def factorial(numero):
    f = 1
    if numero != 0:
        for i in range(1, numero + 1):
            f = f * i
    return f


cantidad = 0
num = int(input("Número (-1 para detener el programa): "))  # Se hicieron más claras las instrucciones
while num != -1:
    print(f"Factorial: {factorial(num)}")
    cantidad += 1
    num = int(input("Número (-1 para detener el programa): "))
print(f"\nSe leyeron {cantidad} números")
# Se cambian los formatos por f-strings (más fáciles de leer para el programador)

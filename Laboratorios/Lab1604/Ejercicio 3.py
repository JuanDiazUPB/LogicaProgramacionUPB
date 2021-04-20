def sumaDigitos(numero):
    suma = 0
    while numero != 0:
        digito = numero % 10
        suma += digito  # Formato simplificado
        numero = numero // 10
    return suma


sumatoria = 0
num = int(input("Número a procesar (0 para detener el proceso): "))  # Instrucciones para detener el programa
while num != 0:
    print("Suma de los dígitos:", sumaDigitos(num))
    sumatoria = sumatoria + num
    num = int(input("Número a procesar: "))
print("\nSumatoria:", sumatoria)
print("Suma de los digitos:", sumaDigitos(sumatoria))

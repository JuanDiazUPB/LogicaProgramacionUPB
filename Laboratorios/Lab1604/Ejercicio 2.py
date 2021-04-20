def sumaDigitos(numero):
    suma = 0
    while numero != 0:
        digito = numero % 10
        suma += digito  # Formato simplificado
        numero = numero // 10
    return suma


num = int(input("Número a procesar (0 para detener el proceso): "))  # Instrucciones para detener el programa
while num != 0:
    print("Suma de los dígitos:", sumaDigitos(num))  # Mejor explicación para el usuario
    num = int(input("Número a procesar: "))

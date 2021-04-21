def primo(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def frecuencia(numero, digito):
    cantidad = 0
    while numero != 0:
        ultDigito = numero % 10
        if ultDigito == digito:
            cantidad += 1
        numero = numero // 10
    return cantidad


def factorial(numero):
    f = 1
    if numero != 0:
        for i in range(1, numero + 1):
            f = f * i
    return f


def sumaDigitos(numero):
    suma = 0
    while numero != 0:
        digito = numero % 10
        suma = suma + digito
        numero = numero // 10
    return suma


mayor = 0
numero = int(input("Introduzca un número primo: "))
while primo(numero):
    print("Suma de los dígitos:", sumaDigitos(numero))
    digito = int(input("Introduzca un dígito (0-9): "))
    if digito > 9:
        print('\nNo se escribió un dígito...\n')  # Una explicación en caso que falle
    else:
        print(f"El {digito} aparece {frecuencia(numero, digito)} veces")
    if numero > mayor:
        mayor = numero
    numero = int(input("Número primo: "))
print(f"\nFactorial del mayor ({mayor}): {factorial(mayor)}")

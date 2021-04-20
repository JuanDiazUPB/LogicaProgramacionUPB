def frecuencia(numero, digito):
    cantidad = 0
    while numero != 0:
        ultDigito = numero % 10
        if ultDigito == digito:
            cantidad += 1
        numero = numero // 10
    return cantidad


num = int(input("Introduzca un número: "))
un_digito = int(input("Introduzca un dígito (0-9): "))  # Se dio mayor claridad a la instrucción
if un_digito > 9:
    print('\nNo se escribió un dígito...')  # Una explicación en caso que falle
else:
    print(f"\nFrecuencia del dígito en el número: {frecuencia(num, un_digito)}")

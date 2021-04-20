def primo(num):
    for i in range(2, num):
        if num % i == 0:  # Si el residuo es 0:
            return False  # El número no es primo
    return True  # Si no, es primo


numero = int(input("Introduzca un número: "))
if primo(numero):
    print("Es primo (solo tiene dos divisores)")
else:
    print("No es primo (tiene más de dos divisores)")

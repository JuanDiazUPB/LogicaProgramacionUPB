def imprimir_tabla(numero):
    # Comenzar en 1
    contador = 1
    while contador <= 10:  # Las tablas de multiplicar son los 10 primeros valores
        resultado = contador * numero
        print("{} x {} = {}".format(numero, contador, resultado))
        # Incrementar contador para no caer en ciclo infinito
        contador += 1


# Se le pide al usuario escribir la tabla que quiera calcular
imprimir_tabla(int(input('Inserte la tabla de multiplicación que quiera calcular: ')))

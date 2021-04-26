numeros = []
while True:
    n = float(input('Inserte los valores a los que quiera calcular su promedio (0 para detener el programa): '))
    if n == 0:
        break
    else:
        numeros.append(n)
        print(f'\nNúmeros escritos: {numeros}\n')

promedio = sum(numeros) / len(numeros)
print(f'El promedio de los valores introducidos es: {round(promedio, 2)}')

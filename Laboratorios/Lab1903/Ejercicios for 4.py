print('Ejercicio 4: Pedir al usuario que ingrese un número entero positivo e imprimir todos los números correlativos entre el ingresado por el usuario y uno menos del doble del mismo.')
n = int(input("Número: "))
for n in range(n, n*2):
    print(n)
print('Ejercicio 9: Dado un número entero positivo, mostrar su factorial.')
numero = int(input("Número: "))
f = 1
if numero != 0:
    for i in range(1,numero+1):
        f = f * i
print("Factorial:", f)

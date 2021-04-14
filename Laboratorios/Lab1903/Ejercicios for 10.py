print('Ejercicio 10: Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci.')
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
for x in range(10):
    print(fib(x))

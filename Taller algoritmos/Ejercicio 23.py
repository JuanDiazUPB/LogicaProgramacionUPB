n = int(input('Introduzca un número: '))
if n < 0:
    print('El número es negativo')
elif n > 0:
    print('El número es positivo')
elif n == 0:
    print('El número es 0')
if n % 2 == 0:
    print('El número es par')
else:
    print('El número es impar')
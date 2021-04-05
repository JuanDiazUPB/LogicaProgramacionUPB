nota1 = float(input('Escriba la nota número 1: '))
nota2 = float(input('Escriba la nota número 2: '))
nota3 = float(input('Escriba la nota número 3: '))
prom = (nota1 + nota2 + nota3) / 3
print('El promedio es:', prom)
if 7 <= prom <= 10:
    print('Promovido')
elif 4 <= prom < 7:
    print('Regular')
else:
    print('No habilitado')

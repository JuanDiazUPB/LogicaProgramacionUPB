n = int(input('Escriba un número: '))
lista = []
for x in range(n, n + 10):
    lista.append(x)
    print(x)
print(f'\nLa suma de los valores es {sum(lista)} y su promedio es {sum(lista) / len(lista)}')

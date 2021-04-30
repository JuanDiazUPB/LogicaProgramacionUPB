n1 = float(input('Introduzca la nota 1: ')) * 0.15
n2 = float(input('Introduzca la nota 2: ')) * 0.2
n3 = float(input('Introduzca la nota 3: ')) * 0.15
n4 = float(input('Introduzca la nota 4: ')) * 0.3
n5 = float(input('Introduzca la nota 5: ')) * 0.2
notas = [n1, n2, n3, n4, n5]
nfinal = sum(notas)
if nfinal <= 2:
    print(f'Su nota final fue {nfinal}, ha reprobado. No hay posibilidad de habilitar...')
elif nfinal < 3:
    print(f'Su nota final fue {nfinal}, ha reprobado.')
elif nfinal >= 3:
    if nfinal >= 4.5:
        print(f'Su nota final fue {nfinal}, ha aprobado. Felicitaciones, su resultado fue excelente!')
    else:
        print(f'Su nota final fue {nfinal}, ha aprobado.')

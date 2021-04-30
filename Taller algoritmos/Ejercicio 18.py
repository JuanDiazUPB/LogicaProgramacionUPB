segundos = int(input('Introduzca la cantidad de segundos: '))
m, s = divmod(segundos, 60)
h, m = divmod(m, 60)
print(f'{h:02d}:{m:02d}:{s:02d}')

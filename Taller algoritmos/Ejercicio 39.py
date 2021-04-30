dsemana = {1: 'Lunes', 2: 'Martes', 3: 'Miércoles', 4: 'Jueves', 5: 'Viernes', 6: 'Sábado', 7: 'Domingo'}
dia = int(input('Digite un número del 1 al 7: '))
print(f'El número introducido corresponde al dia {dsemana.get(dia)}')

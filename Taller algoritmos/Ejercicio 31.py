distancia = int(input('Introduzca la distancia (km) hasta el destino: '))
dias = int(input('¿Cuantos días se va a quedar?: '))
precio = 100000
if distancia <= 1000:
    print(f'\nEl precio del pasaje es {precio} pesos')
else:
    for p in range(1000, distancia):
        precio += 5000
    print(f'\nEl precio del pasaje es {precio} pesos')
if dias > 7:
    precio = precio - precio * 0.15
    print('Como se está quedando más de 7 días, se le aplicará un descuento del 15%!'
          f'\n\nSu nuevo precio es {precio} pesos')

vproducto = int(input('Introduzca el valor del producto: '))
vventa = vproducto + (vproducto * 0.19)
if vventa >= 150000:
    print('Valor superior a 150000 pesos, restando 5% al valor...')
    vventa = vventa - (vventa * 0.05)
print(f'El valor de la venta fue: {vventa}')

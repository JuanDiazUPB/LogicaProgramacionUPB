anio = int(input('Introduzca un año: '))
if (anio % 4) == 0:
    if (anio % 100) == 0:
        if (anio % 400) == 0:
            print(f'{anio} es un año bisiesto')
        else:
            print(f'{anio} no es un año bisiesto')
    else:
        print(f'{anio} es un año bisiesto')
else:
    print(f'{anio} no es un año bisiesto')

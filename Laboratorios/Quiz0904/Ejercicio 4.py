def sumar():  # Definimos la función sumar
    x = a + b
    print(a, "+", b, "=", x)


def restar():  # Definimos la función restar
    x = a - b
    print(a, "-", b, "=", x)


def multiplicar():  # Definimos la función multiplicar
    x = a * b
    print(a, "*", b, "=", x)


def dividir():  # Definimos la función dividir
    x = a / b
    print(a, "/", b, "=", x)


while True:  #
    try:  # Intentamos obtener los datos de entrada
        a = int(input("Ingresa el primer numero: \n"))  #
        b = int(input("Ingresa el segundo numero: \n"))  #
        print("¿Qué cálculo quieres realizar? Escribiste:", a, "y", b, "\n")
        op = str(input(""" 
        1- Sumar
        2- Restar
        3- Multiplicar
        4- Dividir \n"""))  # Ofrecemos las opciones de cálculo que van a llamar a las funciones
    except:  # En caso de error:
        print("Error")
        op = '?'

    if op == '1':  # Si el usuario elige opción 1 llamamos a sumar
        sumar()
        break
    elif op == '2':  # Si el usuario elige opción 2 llamamos a restar
        restar()
        break
    elif op == '3':  # Si el usuario elige opción 3 llamamos a multiplicar
        multiplicar()
        break
    elif op == '4':  # Si el usuario elige opción 4 llamamos a dividir
        dividir()
        break
    else:
        print("Has ingresado un numero de opción erróneo")  # En caso que el número no se encuentre

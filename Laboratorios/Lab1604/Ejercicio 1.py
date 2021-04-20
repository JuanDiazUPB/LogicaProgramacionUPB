def validacion(email):
    for x in email:
        if direccion.endswith("@gmail.com") or direccion.endswith("@hotmail.com") or direccion.endswith("@outlook.com"):
            # endswith valida la ultima parte de la cadena
            return True
    return False


direccion = input("Ingresa tu email: ")
if validacion(direccion):
    print("Dirección válida:", direccion)
else:
    print("Dirección inválida (debe tener @gmail, @hotmail o @outlook)")

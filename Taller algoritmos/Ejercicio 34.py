user = 'MarcosJ'
password = 'camila123'
print('(Usuario: MarcosJ, contraseña: camila123)\n')
u = str(input('Nombre de usuario: '))
p = str(input('Contraseña: '))
if u != user or p != password:
    print('\nNombre de usuario o contraseña incorrectos...')
else:
    print(f'\nBienvenido, {user}')

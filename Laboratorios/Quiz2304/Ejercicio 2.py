A = int(input("¿Cuantos nombres quiere escribir?: "))
A1 = A
B = []
C = []
for i in range(0, A):
    B.append(input(f"Ingresa el nombre de las personas ({A1} restantes): "))
    A1 = A1 - 1
print(B)
for j in range(0, A):
    C.append(len(B[j]))
print(f'La cantidad de letras en cada nombre es (en orden de escritura): {C}')

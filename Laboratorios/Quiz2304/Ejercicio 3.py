subjects = ["Matemáticas", "Física", "Química", "Historia", "Lenguaje"]
scores = []
for subject in subjects:
    score = float(input(f"¿Qué nota has sacado en {subject}?\n"))
    scores.append(score)
for i in range(len(subjects)):
    print(f"En {subjects[i]} has sacado {scores[i]}")
promedio = sum(scores) / len(scores)
print(f'\nTu promedio fue: {promedio}')
if promedio >= 3:
    print('Felicidades, aprobaste!')
else:
    print('Reprobaste...')

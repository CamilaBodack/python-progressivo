ultimo = 0
penultimo = 1
antepenultimo = 1
i = 0
print(0)
print(1)
print(1)

while ultimo <= 500:
    ultimo = penultimo + antepenultimo
    penultimo = antepenultimo
    antepenultimo = ultimo
    i+=1
    print(ultimo)
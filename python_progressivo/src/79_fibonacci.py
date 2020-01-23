posicao = int(input("posição:"))

ultimo = 0
penultimo = 1
antepenultimo = 1

for i in range(posicao):
    ultimo = penultimo + antepenultimo
    penultimo = antepenultimo
    antepenultimo = ultimo
    i+=1
    print(ultimo)

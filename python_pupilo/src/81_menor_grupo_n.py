grupo = int(input("Insira o tamanho do grupo:"))
i = 0
menor = grupo
maior = grupo
soma  = i + maior

for i in range(grupo):
    if i < menor:
        menor = i
print("Menor:",menor, "Maior:", maior, "soma:", soma)


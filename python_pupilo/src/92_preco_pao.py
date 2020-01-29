preco_pao =  float(input("Insira o preço do pão R$:"))

pao = preco_pao

for i in range(50+1):
    paes = pao * i

print("O total de pães será:",paes)

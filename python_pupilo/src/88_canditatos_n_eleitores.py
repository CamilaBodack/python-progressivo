eleitores = int(input("Insira o total de eleitores"))

candidato_1 = 0
candidato_2 = 0
candidato_3 = 0

for i in range(eleitores):
    voto = int(input("1 - Clóvis, 2 -  Nicolas, 3 - Ryuk. \n Digite o número do candidato:"))
    if voto == 1:
        candidato_1 = candidato_1 + 1
    elif voto == 2:
        candidato_2 = candidato_2 + 1
    elif voto == 3:
        candidato_3 = candidato_3 + 1

print("Votos: Clóvis:",candidato_1,"Nícolas:", candidato_2,"Ryuk:", candidato_3)

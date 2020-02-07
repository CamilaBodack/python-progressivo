total_veiculos = 0
total_acidentes = 0
total_menos_acidentes = 0
media_menos_acidentes = 0
mais_acidentes = 0
menos_acidentes = 100000000000
cidade_mais_acidentes = 0
cidade_menos_acidentes = 0
i = 0

for i in range(5):
    cidade = int(input(" #Garopaba - 1 \n #Paulo Lopes - 2 \n #Imbituba - 3 \n #Santo Amaro - 4 \n #Laguna - 5 "))
    veiculos = int(input("Veiculos:"))
    acidentes = int(input("Acidentes de trânsito com vítimas:"))
    total_veiculos = total_veiculos + veiculos
    media_veiculos = total_veiculos/5
    total_acidentes = total_acidentes + acidentes
    media_acidentes = total_acidentes/5
    if acidentes > mais_acidentes:
        mais_acidentes = acidentes
        cidade_mais_acidentes = cidade
    if acidentes < menos_acidentes:
        menos_acidentes = acidentes
        cidade_menos_acidentes = cidade
    if veiculos <= 2000:
        i += 1
        total_menos_acidentes = total_veiculos + veiculos
        media_menos_acidentes = total_acidentes/i

print("Maior índice de acidentes:", mais_acidentes, "cidade número:", cidade_mais_acidentes)
print("Menor índice de acidentes:", menos_acidentes, "cidade número:", cidade_menos_acidentes)
print("Média veículos nas 5 cidades:", media_veiculos)
print("Média nas cidades com < 2000 veículos:", media_menos_acidentes)

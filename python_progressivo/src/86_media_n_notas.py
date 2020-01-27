qtd_medias = int(input("Insira a quantidade de números que deseja aplicar a média"))

notas = 0

for i in range(qtd_medias):
    nota = float(input("Insira a nota"))
    notas = notas + nota
    media = notas/qtd_medias
print("Média geral:", media)

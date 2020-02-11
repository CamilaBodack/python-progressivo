maior_nota = 0
menor_nota = 0
total_notas = 0
media_notas = 0

while True:
    atleta = input("Atleta:")
    for i in range(7):
        notas = float(input("Nota:"))
        total_notas = total_notas + notas
        if notas > maior_nota or i == 0:
            maior_nota = notas
        if notas < menor_nota or i == 0:
            menor_nota = notas
    media_notas = (total_notas - menor_nota - maior_nota)/5
    print("Resultado final:")
    print("Atleta:", atleta)
    print("Melhor nota:", maior_nota)
    print("Pior nota:", menor_nota)
    print("Média:", media_notas)

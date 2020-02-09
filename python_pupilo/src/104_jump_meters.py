maior_salto = 0
menor_salto = 0
maiores_saltos = 0
melhor_atleta = 0
total_saltos = 0

for i in range(2):
    atleta = input("Nome do atleta:")
    for z in range(2):
        salto = float(input("Distância do salto (metros):"))
        total_saltos = total_saltos + salto
        z += 1
        media_saltos = total_saltos/z
    if salto > maior_salto or i == 0:
        maior_salto = salto
        maiores_saltos = maiores_saltos + maior_salto
        melhor_atleta = atleta
    if salto < menor_salto or i == 0:
        menor_salto = salto

print("Atleta:", melhor_atleta)
print("Melhor salto:", maior_salto)
print("Pior salto:", menor_salto)
print("Média dos demais saltos:", media_saltos)
print("Resultado final:")
print(melhor_atleta, ":", maior_salto, "m")

qtd_individuals = int(input("Insira a quantidade de indivíduos:"))

total_ages = 0

for i in range(qtd_individuals):
    age = int(input("Insira a idade do indivíduo:"))
    total_ages = total_ages + age
    media = total_ages/qtd_individuals
if media >= 0 and media <= 25:
    print("Jovens")
elif media >= 26 and media <= 60:
    print("Adultos")
elif media > 60:
    print("Idosos")

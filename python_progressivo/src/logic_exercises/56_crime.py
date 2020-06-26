telefone = int(input("Telefonou para a vítima ?" '\n' "1 - Sim '\n' 0 - Não"))

local = int(input("Esteve no local do crime ?" '\n' "1 - Sim '\n' 0 - Não"))

moradia = int(input("Mora perto da vítima ?" '\n' "1 - Sim '\n' 0 - Não"))

divida = int(input("Devia para a vítima ?"'\n' "1 - Sim '\n' 0 - Não"))

trabalho = int(input("Trabalhou com a vítima ?"'\n' "1 - Sim '\n' 0 - Não"))

total = telefone + local + moradia + divida + trabalho

if total <= 1:
    print("Inocente")
elif total == 2:
    print("Suspeito")
elif total == 3 and total == 4:
    print("Cumplice")
elif total == 5:
    print("Assassino")
else:
    print("Reavaliar")


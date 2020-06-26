cidade_1 = float(input("Insira o valor da população da cidade A:"))
cidade_2 = float(input("Insira o valor da população da cidade B:"))
count = 0

while cidade_1 <= cidade_2:
    cidade_1 = cidade_1 + (cidade_1*0.03)
    cidade_2 = cidade_2 + (cidade_2*0.015)
    count += 1
    print(count)

num_1 = int(input("Insira o primeiro valor:"))
num_2 = int(input("Insira o segundo valor:"))
soma = (num_1 + num_2)


if num_1 > num_2:
    aux = num_1
    num_1 = num_2
    num_2 = aux

num_1 = num_1 + 1

for num in range(num_1,num_2):
        print(num)

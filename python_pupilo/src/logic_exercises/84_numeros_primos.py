num = int(input("Insira o valor:"))

verifica = 0

for i in range(2,num):
    if num % i == 0:
        print("não é primo, multiplo dê:",i)
        verifica +=1

if verifica == 0:

    print("O número",num,"é primo")


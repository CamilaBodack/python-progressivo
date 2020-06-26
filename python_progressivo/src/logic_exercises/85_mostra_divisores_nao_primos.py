num = int(input("Insira o valor:"))

count_primos = 0

for x in range(1,num):
    verifica = 0
    for i in range(2,x):
        if x % i == 0:
            verifica +=1
            count_primos +=1
        if count_primos != 0:
            print(count_primos)

    if verifica == 0:
        print("O número",x,"é primo")

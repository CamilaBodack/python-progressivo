num_1 = float(input("Valor 1"))
num_2 = float(input("Valor 2"))

option = int(input( "1 - Verifica se é par ou impar '\n'"
                    "2 - Verifica se é positivo ou negativo" '\n' "3 - Verifica se inteiro ou decimal"))

if option == 1:
    print("Opção 1 - par ou impar")
    if num_1 % 2 == 0:
        print(num_1,"é par")
    else:
        print(num_1, "é impar")
    if num_2 % 2 == 0:
        print(num_2," é par")
    else:
        print(num_2,"é impar")

if option == 2:
    print("Opção 2 - positivo ou negativo")
    if num_1 < 0:
        print(num_1,"é negativo")
    else:
        print(num_1,"é positivo")
    if num_2 < 0:
        print(num_2, "é negativo")
    else:
        print(num_2,"é positivo")

if option == 3:
    print("Opção 3 - inteiro ou decimal")
    arredondar_1 = round(num_1)
    arredondar_2 = round(num_2)
    if num_1 == arredondar_1:
        print(int(num_1),"é inteiro")
    else:
        print(num_1,"é decimal")
    if num_2 == arredondar_2:
        print(int(num_2),"é inteiro")
    else:
        print(num_2,"é decimal")








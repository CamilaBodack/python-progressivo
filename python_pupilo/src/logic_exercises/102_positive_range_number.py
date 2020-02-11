num = 1
a = 0
b = 0
c = 0
d = 0

while num >= 0:
    num = int(input("Insira o número:"))
    if num <= 25:
        a += 1
        print("Quantidade entre [0 - 25]:", a)
    elif num >= 26 and num <= 50:
        b += 1
        print("Quantidade entre [26 - 50]:", b)
    elif num >= 51 and num <= 75:
        c += 1
        print("Quantidade entre [51 - 75]:", c)
    elif num >= 76 and num <= 100:
        d += 1
        print("Quantidade entre [76 - 100]:", d)
if num < 0:
    print("Fim da leitura.")

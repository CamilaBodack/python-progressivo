num = int(input("Insira o número que será calculado:"))
print("Fatorial de:", num)
print (num,"! = 1", end="")
while num != 0:
    resultado = 1
    count = 1
    while count <= num:
        resultado = resultado * count
        count += 1
        print(".",count, end="")
    print(" = ", resultado)
    break

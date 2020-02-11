cds = int(input("Insira a quantidade de CDs:"))

total = 0

for i in range(cds):
    valor = float(input("Insira o valor do CD:"))
    total = total + valor

print("O valor total gasto na coleção foi R$:",total)

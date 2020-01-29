itens = int(input("Insira a quantidade de produtos: "))

if itens <= 50:
    for i in range(itens):
        total = 1.99 * itens
    print("O total a pagar é R$:",total)
else:
    print("Quantidade de itens não permitida.")

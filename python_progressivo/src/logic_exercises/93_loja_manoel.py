item = -1
total = 0
i = 1

while item != 0:
    item = int(input("Quantidade de itens:"))
    valor_item = float(input("Insira o valor do item R$:"))
    total = total + (valor_item * item)
    print("Produto", i, "R$:", valor_item)
    print("Total R$", round(total))
    i += 1

else:
    print("Lojas CatKitten - Total a pagar R$:", total)
    pagamento = float(input("Insira o valor do pagamento R$"))
    troco = pagamento - total
    print("Troco R$", troco)

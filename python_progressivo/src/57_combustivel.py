combustivel = int(input("1 - Alcool '\n' 2 - Gasolina"))

if combustivel == 1:
    litros = float(input("Litros"))
    if litros <= 20:
        preco = (1.9*litros)
        desconto = preco* 0.03
        pagar = preco - desconto
        print("Total a pagar R$: ", pagar)
    else:
        preco = (1.9*litros)
        desconto = preco * 0.05
        pagar = preco - desconto
        print("Total a pagar R$:", pagar)

if combustivel == 2:
    litros = float(input("Litros"))
    if litros <= 20:
        preco = (2.5 * litros)
        desconto = preco * 0.04
        pagar = preco - desconto
        print("Total a pagar R$:", pagar)
    else:
        preco = (2.5 * litros)
        desconto = preco * 0.06
        pagar = preco - desconto
        print("Total a pagar R$:", pagar)






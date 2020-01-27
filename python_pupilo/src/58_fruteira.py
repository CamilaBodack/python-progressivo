peso_morango = float(input("Peso morango"))
peso_maca = float(input("Peso maca"))
total = peso_morango + peso_maca

if total <= 5:
    preco_morango = peso_morango * 2.5
    preco_maca = peso_maca * 1.8
    total = preco_morango + preco_maca
    print("Menor que 5 kg - Total R$ %.2f:" %total)

elif total > 5 and total < 8:
    preco_morango = peso_morango * 2.2
    preco_maca = peso_maca * 1.5
    total = preco_morango + preco_maca
    print("Maior que 5 e menor que 8 kg  - Total R$ %.2f" %total)

elif total > 8 or total > 25:
    total = total - 0.1
    print("Compra acima de 8 kg ou R$ 25 - Total R$ %.2f" %total)
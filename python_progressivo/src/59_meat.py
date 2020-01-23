cartao_desconto = int(input("Possui cartão de desconto ? 1 - Sim '\n' 2 - Não"))

opcao_carne = int(input("1 - Filé duplo '\n' 2 - Alcatra '\n' 3 - Picanha"))

if opcao_carne == 1:
     peso_file_duplo = float(input("Peso filé duplo"))
elif opcao_carne == 2:
     peso_alcatra = float(input("Peso alcatra"))
elif opcao_carne == 3:
     peso_picanha = float(input("Peso picanha"))
else:
    print("Opção inválida")


if cartao_desconto == 1:

    if opcao_carne == 1 and peso_file_duplo < 5:
        preco_file_duplo = peso_file_duplo*4.9
        desconto = preco_file_duplo * 0.05
        total = preco_file_duplo - desconto
        print("Menor de 5 kg - com desconto - Total filé R$ %.2f" %total)

    elif opcao_carne == 1 and peso_file_duplo > 5:
         preco_file_duplo = peso_file_duplo * 5.8
         desconto = preco_file_duplo * 0.05
         total = preco_file_duplo - desconto
         print("Acima 5 kg - Total filé R$ %.2f" % total)

    elif opcao_carne == 2 and peso_alcatra < 5:
         preco_alcatra = peso_alcatra * 5.9
         desconto = preco_alcatra * 0.05
         total = preco_alcatra - desconto
         print("Total com desconto alcatra R$ %.2f" %total)

    elif opcao_carne == 2 and peso_alcatra > 5:
         preco_alcatra = peso_alcatra * 6.8
         desconto = preco_alcatra * 0.05
         total = preco_alcatra - desconto
         print("Total com desconto alcatra R$ %.2f" %total)

    elif opcao_carne == 3 and peso_picanha < 5:
         preco_picanha = peso_picanha * 6.9
         desconto = preco_picanha * 0.05
         total = preco_picanha - desconto
         print("Total com desconto picanha R$ %.2f" %total)

    elif opcao_carne == 3 and peso_picanha > 5:
         preco_picanha = peso_picanha * 7.8
         desconto = preco_picanha * 0.05
         total = preco_picanha - desconto
         print("Total com desconto picanha R$ %.2f" %total)

if cartao_desconto == 2:

    if opcao_carne == 1 and peso_file_duplo < 5:
        preco_file_duplo = peso_file_duplo*4.9
        print("Sem cartao - Menor de 5 kg - Total filé R$ %.2f" %preco_file_duplo)

    elif opcao_carne == 1 and peso_file_duplo > 5:
         preco_file_duplo = peso_file_duplo*5.8
         print("Sem  cartao - Menor de 5 kg - Total filé R$ %.2f" %preco_file_duplo)

    elif opcao_carne == 2 and peso_alcatra < 5:
         preco_alcatra = peso_alcatra * 5.9
         print(" Sem cartao - menos de 5 kg - Total alcatra R$ %.2f" %preco_alcatra)

    elif opcao_carne == 2 and peso_alcatra > 5:
         preco_alcatra = peso_alcatra * 6.8
         print("Sem cartao - acima de 5 kg - Total alcatra R$ %.2f" %preco_alcatra)

    elif opcao_carne == 3 and peso_picanha < 5:
         preco_picanha = peso_picanha * 6.9
         print(" Sem cartao - menos de 5 kg - Total picanha R$ %.2f" %preco_picanha)

    elif opcao_carne == 3 and peso_picanha > 5:
         preco_picanha = peso_picanha * 7.8
         print("Sem cartão - acima de 5 kg - Total picanha R$ %.2f" %preco_picanha)
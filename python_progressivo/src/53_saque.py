'''notas de 100, 50, 10, 5, 2'''

valor_saque = int(input("Insira o valor do saque"))

if valor_saque%2 != 0:
    print("Não é permitido sacar esse valor")

elif (valor_saque >= 10) and (valor_saque <= 600):
    notas_100 = int(valor_saque/100)
    valor_saque = valor_saque -(notas_100*100)
    notas_50 = int(valor_saque/50)
    valor_saque = valor_saque - (notas_50*50)
    notas_10 = int(valor_saque/10)
    valor_saque = valor_saque - (notas_10*10)
    notas_2 = int(valor_saque / 2)
    valor_saque = valor_saque - (notas_2*2)
    notas_5 = int(valor_saque / 5)
    print("Notas de R$ 100:", notas_100, ",Notas de R$ 50:", notas_50,", Notas de R$ 10:", notas_10, ", Notas de R$ 5",
          notas_5,"Notas de R$ 2:", notas_2)
else:
    print("Valor de saque não permitido")



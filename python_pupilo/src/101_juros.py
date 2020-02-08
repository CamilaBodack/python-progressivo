divida = float(input("Valor da dívida:"))
num_parcelas = int(input("Parcelas:"))

for i in range(1):

    juros_3 = divida * 0.1
    juros_6 = divida * 0.15
    juros_9 = divida * 0.2
    juros_12 = divida * 0.25
    parcela_juros_3 = divida + juros_3
    parcela_juros_6 = divida + juros_6
    parcela_juros_9 = divida + juros_9
    parcela_juros_12 = divida + juros_12
    print("Valor dívida |", "Juros |", "Parcelas |", "Valor parcelas R$")
    print(divida, "  |  ",      0,  "    |  ", 1, "  |   ", divida)
    print(divida, "  |  ",   juros_3, "  |  ", 3, "  |  ", parcela_juros_3)
    print(divida, "  |  ",   juros_6, "  |  ", 6, "  |  ", parcela_juros_6)
    print(divida, "  |  ",   juros_9, "  |  ", 9, "  |  ", parcela_juros_9)
    print(divida, "  |  ",   juros_12, " |  ", 12, " | ", parcela_juros_12)

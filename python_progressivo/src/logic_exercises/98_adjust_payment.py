salario = 1000
ajuste = 0.015 * salario
salario = salario + ajuste
print("Primeiro salário R$:", 1000, "após primeiro ajuste R$:", salario)
count = 0
i = 0

for count in range(25):
    i += 2
    count += 1
    ajuste = salario * (0.015 * i)
    salario = salario + ajuste
    print("Tempo trabalhado (anos):", count, "salário ajustado:", "%.2f" % salario)

for i in range(1):
    salario = float(input("Insira seu salário inicial:"))
    for count in range(26):
        i += 2
        count += 1
        ajuste = salario * (0.015 * i)
        salario = salario + ajuste
        print("Tempo trabalhado (anos):", count, "salário ajustado:", "%.2f" % salario)
    break

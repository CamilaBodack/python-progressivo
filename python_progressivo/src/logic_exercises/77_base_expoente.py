base = int(input("Insira o valor da base:"))
expoente = int(input("Insira o valor do expoente:"))

for exp in range(expoente):
    calculo = exp * exp
    resultado =  base * calculo

print(resultado)

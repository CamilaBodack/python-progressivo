primeiro = 0
maior = primeiro

primeiro = int(input("Insira o primeiro valor:"))

for num in range(4):
    numeros =  int(input("Insira o valor:"))
    if numeros > maior:
        maior = numeros
print("O maior valor é:",maior)

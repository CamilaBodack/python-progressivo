primeiro = 0
maior = primeiro

primeiro = int(input("Insira o primeiro valor:"))

for num in range(4):
    numeros =  int(input("Insira o valor:"))
    primeira_soma = numeros + primeiro
    segunda_soma = primeira_soma + numeros
    terceira_soma = segunda_soma + numeros
    quarta_soma = terceira_soma + numeros
    ultima_soma = quarta_soma + numeros
    media = ultima_soma/5

    if numeros > maior:
        maior = numeros
        
print("O maior valor é:",maior)
print("O valor da soma é:", ultima_soma)
print(" E o valor da média é:", media)
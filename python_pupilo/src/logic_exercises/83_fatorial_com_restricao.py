numero = int(input("Insira o número para calcular a fatorial:"))

if numero < 0 or numero > 16:
     print("Valor fora da faixa calculavel")
else:
    while numero !=0 :
        resultado = 1
        count = 1
        while count <= numero:
            resultado *= count
            count += 1
        print(resultado)
        numero = int(input("Insira o número para calcular a fatorial:"))

numero = int(input("Insira o número"))

#1000 mostrar dezena, centena e milhar.

unidade = numero % 10
numero = (numero - unidade)/10
dezena = numero % 10
numero = (numero - dezena)/10
centena = numero

dezena = int(dezena)
centena = int(centena)

print("Unidade :",unidade, ",dezena:", dezena, ",centena:", centena)
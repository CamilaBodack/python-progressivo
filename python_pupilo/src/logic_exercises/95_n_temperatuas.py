total = 0
menor = 0
maior = 0

temperaturas = int(input("Quantas temperaturas deseja inserir ?"))
for i in range(temperaturas):
    temperatura = float(input("Temperatura em °C:"))
    if i == 0:
        menor = temperatura
        maior = temperatura
    if temperatura < menor:
        menor = temperatura
    if temperatura > maior:
        maior = temperatura
    total = total + temperatura
    media = total/temperaturas
print("Maior:", maior, "Menor:", menor, "Média:", media)

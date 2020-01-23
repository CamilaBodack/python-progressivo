''' tem que usar dois contadores separados para funcionar'''
count_par = 0
count_impar = 0

for count in range (10):
    numero =  int(input("Insira o valor:"))
    if numero % 2 == 0:
        count_par += 1
    else:
        count_impar +=1

print("pares",count_par)
print("impar",count_impar)





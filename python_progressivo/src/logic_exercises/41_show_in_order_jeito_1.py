menor = 0
meio = 0
maior = 0

a = int(input("primeiro"))
maior = a

b = int(input("segundo"))

if (b > maior):
    meio = a
    maior = b
else:
    meio = b
        
c = int(input("terceiro"))

if (c > maior):
    menor = a
    meio = b
    maior = c

elif (c > meio):
    menor = b
    meio = c
else:
    menor = c
    
print(maior,meio,menor)
    



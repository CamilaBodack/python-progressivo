year = int(input("Ano"))

if year % 4 == 0 and year % 100 != 0:
    print("Ano bissexto")
    
else:
    print("Não é bissexto")

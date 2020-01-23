day = int(input("Dia"))
month = int(input("Mês"))
year = int(input("Ano"))

if day >= 1 and day <= 31 and month >= 1 and month <= 12:
    if year % 4 and month == 2 and day < 29:
        print(day,"/",month,"/",year)
    else:
        print("Data inválida")
    
                  

                  








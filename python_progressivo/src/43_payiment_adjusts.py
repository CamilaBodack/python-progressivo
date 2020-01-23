pay = float(input("Valor do salário"))

if  pay <= 280:
    new = pay+((pay*20)/100)
    print("Antigo salario R$:",pay, "Com 20% aumento, gerando o valor de",(pay*20)/100, "ficou R$:",new )

elif pay >= 280 and pay <= 700:
    new = pay+((pay*15)/100)
    print("Antigo salario R$:",pay, "Com 15% aumento, gerando o valor de",(pay*15)/100, "ficou R$:",new )

elif pay >= 700 and pay <= 1500:
    new = pay+((pay*10)/100)
    print("Antigo salario R$:",pay, "Com 10% aumento, gerando o valor de",(pay*10)/100, "ficou R$:",new )

else:
    new = pay+((pay*5)/100)
    print("Antigo salario R$:",pay, "Com 5% aumento, gerando o valor de",(pay*5)/100, "ficou R$:",new )
    
    
    
    

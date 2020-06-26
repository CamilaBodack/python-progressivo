import math

a = int(input("Insira o primeiro"))
b = int(input("Insira o segundo"))
c = int(input("Insira o terceiro"))

# baskara
# ax² + bx + c

delta = (b**b) - (4 * a * c)

#x = -b +- raiz/2*a

if delta < 0:
    print("Não há raizes reais, encerrando")

elif delta == 0:
    print("Possui apenas uma raiz real")

else:
     raiz = math.sqrt(delta)
     x_1 = (-b + raiz)/(2*a)
     x_2 = (-b - raiz)/(2*a)
     print("X¹ =", x_1, "X² =",x_2)
            
        

    

    

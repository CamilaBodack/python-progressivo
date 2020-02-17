import random


class CaraCoroa():
    def __init__(self):
        self.lado = 'Cara'

    def dado(self):
        if (random.randint(0, 1)) % 2 == 0:
            self.lado = 'Cara'
            return self.lado
        else:
            self.lado = 'Coroa'
            return self.lado


moeda = CaraCoroa()
menu = 1

while menu:
    menu = int(input("1 - Jogar novamente \n"
                     "2 - Sair"))
    if menu == 1:
        print(moeda.dado())
    elif menu == 2:
        print("Finalizado.")

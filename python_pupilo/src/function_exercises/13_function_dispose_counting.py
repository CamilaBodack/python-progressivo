def dispose_number(num):
    for i in range(1, num+1):
        for j in range(i):
            print(i, " ", end="")
            print(" ")


def ask_number():
    num = int(input("Insert number:"))
    dispose_number(num)


ask_number()

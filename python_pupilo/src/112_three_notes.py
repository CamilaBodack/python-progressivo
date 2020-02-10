def media(total):
    media = total/4
    print("Media:", media)


total = 0
for i in range(4):
    nota = float(input("Insira a nota:"))
    total = total + nota

media(total)

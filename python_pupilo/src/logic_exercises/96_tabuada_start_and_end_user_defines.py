num = int(input("Tabuada de:"))
inicio = int(input("Inícia em:"))
termina = int(input("Termina em:"))

if termina < inicio:
    print("O valor final não pode ser inferior ao inicial.")

else:
    for i in range(inicio, termina):
        resultado = num * i
        print(num, " x ", i, " = ", resultado)

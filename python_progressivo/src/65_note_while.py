note = float(input("Insira a nota:"))

while note not in range(11):
    note = float(input("\033[1;31m[-] " + "Insira a nota:" + "\033[m"))
else:
    print("\033[1;32m " + "Valor inserido com sucesso!" + "\033[m")

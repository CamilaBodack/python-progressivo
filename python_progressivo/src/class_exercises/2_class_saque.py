class Conta():
    saldo = 0.0

    def __init__(self):
        print("Conta criada.")

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            print("O valor mínimo de depósito é R$ 1")

    def saque(self, valor):
        if valor > self.saldo:
            print("Não há saldo suficiente")
        elif valor > 0 and valor <= self.saldo:
            self.saldo -= valor

    def saldos(self):
        return self.saldo
dic = []
dic 2 = dic

nova_conta = Conta()

opcao = True

while opcao:
    print("0 - Sair")
    print("1 - Deposito")
    print("2 - Saldo")
    print("3 - Saque")
    opcao = int(input())
    if opcao == 0:
        print("Finalizando...")
    elif opcao == 1:
        valor = int(input("Valor do depósito:"))
        nova_conta.deposito(valor)
    elif opcao == 2:
        print("Saldo R$:", nova_conta.saldos())
    elif opcao == 3:
        valor = int(input("Valor do saque:"))
        nova_conta.saque(valor)

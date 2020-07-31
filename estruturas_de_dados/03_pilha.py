'''
Pilhas: o primeiro item que entra é o último a sair da estrutura.
'''


class Pilha:
    def __init__(self):
        self.pilha = []

    def insere(self, dados):
        return self.pilha.append(dados)

    def remove(self):
        if not self.isEmpty():
            return self.pilha.pop()
        else:
            return None

    def topo(self):
        if not self.isEmpty():
            return self.pilha[-1]
        else:
            return None

    def pilha_inteira(self):
        return self.pilha

    def isEmpty(self):
        if (len(self.pilha) == 0):
            return True
        else:
            return False


nova_pilha = Pilha()
nova_pilha.insere(1)
nova_pilha.insere(2)
nova_pilha.insere(3)
nova_pilha.insere(1)
nova_pilha.insere(3)
nova_pilha.insere(2)
print(nova_pilha.topo())

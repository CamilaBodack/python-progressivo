'''
Pilhas: o primeiro item que entra é o último a sair da estrutura.
'''


class Pilha:
    def __init__(self):
        self.pilha = []

    def insere(self, dados):
        return self.pilha.append(dados)

    def remove(self):
        return self.pilha.pop()

    def topo(self):
        return self.pilha[-1]


nova_pilha = Pilha()
nova_pilha.insere(1)
nova_pilha.insere(2)
nova_pilha.insere(3)
nova_pilha.remove()
print(nova_pilha.topo())

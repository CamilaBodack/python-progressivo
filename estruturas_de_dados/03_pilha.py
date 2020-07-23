'''
Pilhas: o primeiro item que entra é o último a sair da estrutura.
'''

class Pilha:
    def __init__(self):
        self.pilha = []

    def push(self, dados):
        self.pilha.append(dados)

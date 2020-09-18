
class No:

	def __init__(self, chave):
		self.chave = chave
		self.leftChild = None
		self.rightChild = None

	def getChave(self):
		return self.chave

	def setChave(self, chave):
		self.chave = chave

	def getLeft(self):
		return self.leftChild

	def getRight(self):
		return self.rightChild

	def setLeft(self, leftChild):
		self.leftChild = leftChild

	def setRight(self, rightChild):
		self.rightChild = rightChild


class ArvoreBinaria:

	def __init__(self):
		self.raiz = None

	def vazio(self):
		if self.raiz == None:
			return True
		return False

	def insere(self, chave):  # cria no
		no = No(chave)

		if self.vazio():  # verifica se o no esta vazio
			self.raiz = no
		else:  # se a arvore não esta vazia insere o valor da chave
			no_pai = None
			no_atual = self.raiz

			while True:

				if no_atual != None:
					no_pai = no_atual
					if no.getChave() < no_atual.getChave():  # ira para a esquerda
						no_atual = no_atual.getLeft()
					else:
						no_atual = no_atual.getRight()  # vai para a direita
				else:
					if no.getChave() < no_pai.getChave():
						no_pai.setLeft(no)
					else:
						no_pai.setRight(no)
					break


	def mostra_pre_ordem(self, no_atual):  # mostra em pre ordem raiz da esq p direita
		if no_atual != None:
			print('%d' % no_atual.getChave(), end=" ")
			self.mostra_pre_ordem(no_atual.getLeft())
			self.mostra_pre_ordem(no_atual.getRight())

	def getRaiz(self):
		return self.raiz

arvore = ArvoreBinaria()
arvore.insere(8)
arvore.insere(3)
arvore.insere(1)
arvore.insere(6)
arvore.insere(4)
arvore.insere(7)
arvore.insere(10)
arvore.insere(14)
arvore.insere(13)

arvore.mostra_pre_ordem(arvore.getRaiz())

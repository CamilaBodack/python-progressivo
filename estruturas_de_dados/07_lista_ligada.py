''' Os elementos (objetos, nodes etc), possuem a referência do próximo
elemento e de uma informação
'''
class Node:

	def __init__(self, label):
		self.label = label
		self.next = None

	def getLabel(self):
		return self.label

	def setLabel(self, label):
		self.label = label

	def getNext(self):
		return self.next

	def setNext(self, next):
		self.next = next

class LinkedList:

	def __init__(self):
		self.first = None
		self.last = None
		self.len_list = 0

	def push(self, label, index):
		if index >= 0:
			node = Node(label)

			if self.empty():  # verifica se a sequencia esta vazia
				self.first = node
				self.last = node
			else:
				if index == 0:
					node.setNext(self.first)  # insere no início
					self.first = node
				elif index >= self.len_list:
					self.last.setNext(node)  # insere no final
				else:
					prev_node = self.first
					curr_node = self.first.getNext()
					curr_index = 1

					while curr_node != None:
						if curr_index == index:
							node.setNext(curr_node)  # seta o nó atual para o prox
							prev_node.setNext(node)  # seta o node como o prox do prev node
							break

						prev_node = curr_node
						curr_node = curr_node.getNext()
						curr_index += 1

					self.len_list += 1 # finaliza atualizano tamanho da lista

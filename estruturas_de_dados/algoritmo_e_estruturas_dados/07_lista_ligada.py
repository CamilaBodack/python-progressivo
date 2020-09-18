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

		def pop(self, index):
			if not self.empty() and index >= 0 and index < self.len_list:
				flag_remove = False

				if self.first.getNext() == None:
					self.first = None
					self.last = None
					flag_remove = True
				elif index == 0:
					self.first = self.first.getNext()
					flag_remove = True
				else:
					prev_node = self.first
					curr_node = self.first.getNext()
					curr_index += 1

					while curr_node != None:
						if index == curr_node:
							prev_node.setNext(curr_node.getNext())
							curr_node.setNext(None)
							flag_remove = True
							break

						prev_node = curr_node
						curr_node = curr_node.getNext()
						curr_index += 1

				if flag_remove:
					self.len_list -= 1


		def empty(self):
			if self.first == None:
				return True
			return False

		def length(self):
			return self.len_list

		def show(self):
			curr_node = self.first

		while curr_node != None:
			print(curr_node.getLabel(), end=' ')
			curr_node = curr_node.getNext()
		print('')

lista = LinkedList()

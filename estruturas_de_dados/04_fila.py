'''first in first out
'''

class Fila:

	def__init__(self):
		self.fila =  []
		self.len_fila = 0

	def push(self, novo_item):
		self.fila.append(novo_item)
		self.len_fila += 1

	def is_empty(self):
		if self.len_fila ==0:
			return True
		else:
			return False

	def pop(self):
		if not self.is_empty():
			return self.len_fila(0)

	def length_fila(self):
		return self.len_fila

	def first_element(self):
		if not self.is_empty():
			return self.fila[0]

'''first in first out
'''

class Fila:

	def __init__ (self):
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
			return self.fila.pop(0)

	def length_fila(self):
		return self.len_fila

	def first_element(self):
		if not self.is_empty():
			return self.fila[0]

fila_filhote = Fila()
fila_filhote.push(1)
fila_filhote.push(2)
fila_filhote.push(3)
fila_filhote.push(4)
fila_filhote.push(5)
fila_filhote.pop()
print(fila_filhote.first_element())

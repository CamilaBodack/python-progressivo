'''double ended queue
pode inserir ou remover utilizando as duas pontas
'''

class Deque:

	def __init__(self):
		self.deque = []
		self.len = 0

	def is_empty(self):
		if self.len == 0:
			return True
		else:
			return False

	def push_to_front(self, item):
		self.deque.insert(0, item)
		self.len += 1

	def push_back(self, item):
		self.deque.insert(self.len, item)
		self.len += 1

	def pop_front(self):
		if not self.is_empty():
			self.deque.pop(0)
			self.len -= 1

	def pop_back(self):
		if not self.is_empty():
			self.deque.pop(self.len -1)
			self.len -= 1

	def first_element(self):
		if not self.is_empty():
			return self.deque[0]

	def last_element(self):
		if not self.is_empty():
			return self.deque[-1]

	def show_deque(self):
		return self.deque


new_deque = Deque()
new_deque.push_to_front(1)
new_deque.push_to_front(2)
print(new_deque.show_deque())

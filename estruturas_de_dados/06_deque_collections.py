from collections import deque

new_deque = deque()
new_deque.append(1)  # adiciona do lado direito do deque
new_deque.appendleft(2)  # adiciona do lado esquerdo
new_deque.pop()  # remove último elemento do lado direito
new_deque.popleft()  # remove último elemento do lado esquerdo
new_deque.remove()  # remove o elemento independente de sua posição



print(new_deque)

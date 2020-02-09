num = int(input("Número final da sequencia:"))
a = 1
b = 1
soma_a = 0
soma_b = 0

while a < num and b < num-1:
    a += 1
    soma_a = soma_a + a
    b += 2
    soma_b = soma_b + b
    print(a, "/", b)
print("Soma termos:", "A:", soma_a, "B:", soma_b)

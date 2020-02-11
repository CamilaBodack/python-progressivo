num = int(input("Número final da sequencia:"))
a = 1
b = 1

while a < num and b < num-1:
    a += 1
    b += 2
    print(a, "/", b)

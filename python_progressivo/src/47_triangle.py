a = float(input("Lado a"))
b = float(input("Lado b"))
c = float(input("Lado c"))

if (a + b) > c and (c + b) > a and (a + c) > b:
    print("é um triangulo")

    if a == b or a == c or c == b:
        print("isosceles")

    elif a == b and b == c and c == a:
        print("equilatero")

    else:
        print("escaleno")
        
else:
    print("não é um triangulo")

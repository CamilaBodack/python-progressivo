def three_args(x, y, z):
    return x + y + z


def media(a, b, c):
    soma = three_args(a, b, c)
    media = soma/3
    return media


first = float(input("Value 1:"))
second = float(input("Value 2:"))
third = float(input("Value 3:"))
soma = three_args(first, second, third)

print("Result sume:", soma, "media:", media(first, second, third))

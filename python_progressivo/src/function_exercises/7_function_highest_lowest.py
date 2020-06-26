def highest(d, e, f):
    highest = 0
    if d > highest:
        highest = d
    if e > highest:
        highest = e
    if f > highest:
        highest = f
    return highest


def lowest(x, y, z):
    lowest = x
    if y < lowest:
        lowest = y
    if z < lowest:
        lowest = z
    return lowest


a = int(input("Insert first value:"))
b = int(input("Insert second value:"))
c = int(input("Insert trird value:"))

print("Highest value of three:", highest(a, b, c), "lowest value:", lowest(a, b, c))

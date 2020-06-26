def dado():
    import random
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    for i in range(1000000):
        dado = random.randint(1, 6)
        if dado == 1:
            a += 1
        elif dado == 2:
            b += 1
        elif dado == 3:
            c += 1
        elif dado == 4:
            d += 1
        elif dado == 5:
            e += 1
        elif dado == 6:
            f += 1
    print("1:", a, "2:", b, "3:", c, "4:", d, "5:", e, "6:", f)


dado()

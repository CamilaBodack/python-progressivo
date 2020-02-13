def add_fee(cost, tax):
    cost = float(input("Insert value:"))
    while True:
        a = tax * cost
        b = cost + a
        print("Product value + fee:", b)
        add_fee(cost, tax)

def add_fee(cost, tax):
    a = tax * cost
    b = cost + a
    return 'Product + tax', b


cost = float(input("Insert value:"))
tax = float(input("Insert tax"))
total = add_fee(cost, tax)
print(total)

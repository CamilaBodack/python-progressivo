def perfect_number(num):
    total = 0
    for i in range(1, num):
        if num % i == 0:
            aux = i
            total = total + aux
    if total % num == 0:
        print("Perfect number")
    else:
        print("Non perfect number")


num = int(input("Insert number:"))
perfect_number(num)

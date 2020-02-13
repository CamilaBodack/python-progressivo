def negative(num):
    if num < 0:
        return True
    else:
        return False


num = int(input("Insert number:"))
returno = negative(num)
if returno:
    print("Negative")
else:
    print("Positive")

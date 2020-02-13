def negative(num):
    if num < 0:
        print("Negative")
        return True
    else:
        print("Positive")
        return False


num = int(input("Insert number:"))
negative(num)

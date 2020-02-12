def fibonacci():
    num = int(input("Insert number:"))
    i = 0
    last = 0
    penult = 1
    antepenult = 1
    print("1")
    print("1")
    while True:
        if last < num:
            last = penult + antepenult
            penult = antepenult
            antepenult = last
            print(last)
            i += 1
        else:
            break


fibonacci()

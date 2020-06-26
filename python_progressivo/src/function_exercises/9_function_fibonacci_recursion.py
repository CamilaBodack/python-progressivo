def fibonacci():
    num = int(input("Insert number:"))
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
        else:
            break


fibonacci()

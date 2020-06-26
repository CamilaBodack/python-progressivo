def primo():
    num = int(input("Insert number:"))
    for i in range(num):
        verify = 0
        for j in range(i):
            if j > 1 and i % j == 0:
                verify += 1
        if verify == 0:
            print(i)


primo()

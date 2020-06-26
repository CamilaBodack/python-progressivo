#!/usr/bin/env python3
def dispose_number(num):
    for i in range(1, num+1):
        for j in range(i):
            print(i, " ", end="")
            print(" ")


num = int(input("Insert number:"))
dispose_number(num)

'''
Task
Read two integers from STDIN and print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.

'''

num_1 = int(input("Input first number:"))
num_2 = int(input("Input second number"))

sum = num_1 + num_2
menos = num_1 - num_2
multip = num_1 * num_2

print(sum)
print(menos)
print(multip)

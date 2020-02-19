'''
Task
Read two integers and print two lines.
The first line should contain integer division,
// . The second line should contain float division,  / .
You don't need to perform any rounding or formatting operations.
Input Format
The first line contains the first integer,
he second line contains the second integer.
Output Format
Print the two lines as described above. '''

num_1 = int(input())
num_2 = int(input())


int_division = int(num_1/num_2)
float_division = float(num_1/num_2)

print(int_division)
print(float_division)

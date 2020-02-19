'''
Task
You are given the year, and you have
to write a function to check if the year is leap or not.
Note that you have to complete the
function and remaining code is given as template.
'''


def leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


year = int(input())
leap_year(year)

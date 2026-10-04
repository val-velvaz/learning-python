"""
The first century spans from the year 1 up 
to and including the year 100, the second 
century - from the year 101 up to and 
including the year 200, etc.

Task
Given a year, return the century it is in.

Examples
1705 --> 18
1900 --> 19
1601 --> 17
2000 --> 20
2742 --> 28
Note: this kata uses strict construction 
as shown in the description and the examples, 
you can read more about it here
"""
def calculate_year(year):
    if year % 100 != 1:
        return((year // 100) + 1)
    else:
        return((year // 100))


print(calculate_year(1705))
print(calculate_year(201))
print(calculate_year(200))



print(1708 // 100)
centuries = [i for i in range(1, 2100, 100)]
def calculate_year(year):
    i = 1
    for century in range(len(centuries)):
        if year >= century:
            i = i + 1
        else:
            return i
        
    print("century not in range")


print(calculate_year(208))


def century(year):
    step = 100
    centuries = [i for i in range(1, 2100, 100)]


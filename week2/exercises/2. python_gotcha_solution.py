# If we want an empty list as a potential default argument value,
# we can use None as a special value to indicate we did not receive
# anything. After we check whether an argument was provided
# we can instantiate a new list if it wasn't.

def createStudent(name, age, grades=None):
    if grades is None:
        grades = []
    return {
        'name' : name,
        'age' : age, 
        'grades' : grades
    }

def addGrade(student, grade):
    student['grades'].append(grade)
    print(student['grades'])

chrisley = createStudent('Chrisley', 15)
dallas = createStudent('Dallas', 16)

addGrade(chrisley, 90)
addGrade(dallas, 100)

addGrade(chrisley, 89)
addGrade(dallas, 94)

from constraint import *

problem = Problem()
problem.addVariable('Doctor', ['Doc1', 'Doc2', 'Doc3'])
problem.addVariable('Shift', ['Day1-shift1','Day1-shift2', 'Day1-shift3', 'Day2-shift1', 'Day2-shift2', 'Day2-shift3'])

def constraints_func(Doctor, Shift):
    CONSTRAINTS = [
        ("Doc1", "Day1-shift2"),
        ("Doc2", "Day2-shift3"),
        ("Doc3", "Day1-shift1"),
        ("Doc3", "Day1-shift3")
    ]


    for doctor, shift in CONSTRAINTS:
        if doctor == Doctor and shift == Shift:
            return False

    return True


problem.addConstraint(constraints_func, ['Doctor', 'Shift'])

for solution in problem.getSolutions():
    print(solution)




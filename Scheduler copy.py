from calendar import monthrange
from constraint import *
from datetime import datetime


from ShiftOfSchedule import ShiftOfSchedule
from Doctor import Doctor
from Leave import Leave


class Scheduler:
    def __init__(self, doctors, shift_cat, num_doctors):
        self.doctors = doctors
        self.shift_cat = shift_cat
        self.num_doctors = num_doctors
    
    def get_all_shifts(self, year, month):
        first_day, num_days = monthrange(year, month)
        shifts = []
        for i in range(num_days):
            day = i + 1
            # date = str(year) + "-" + str(month) + "-" + str(day)
            date = datetime(year, month, day)
            for j in range(len(self.shift_cat)):
                shift = ShiftOfSchedule(date, self.shift_cat[j], self.num_doctors[self.shift_cat[j]])
                shifts.append(shift)

        self.shifts = shifts
    
    def constraints_func(self, Doctor, Shift):
        if Doctor.is_a_leave(Shift):
            return False
        return True

    def create(self):
        self.get_all_shifts(2022, 12)
        
        problem = Problem()
        problem.addVariable('Doctor', self.doctors)
        problem.addVariable('Shift', self.shifts)

        problem.addConstraint(self.constraints_func, ['Doctor', 'Shift'])
        
        for i in range(self.shifts):
            problem.addConstraint()

        solution = problem.getSolutions()
        return solution

leaves = {"hasini": [Leave('2022-12-01', ["morning", "evening"])]}
hasini = Doctor("hasini")
hasini.add_leave(Leave(datetime(2022, 12, 1), ["morning", "evening"]))
hasini.add_leave(Leave(datetime(2022, 12, 2), ["morning"]))

theshan = Doctor("theshan")
theshan.add_leave(Leave(datetime(2022, 12, 3), ["evening"]))
num_doctors = {"morning": 3, "evening": 2, "night": 1}
scheduler = Scheduler([hasini, theshan], ["morning", "evening", "night"], num_doctors)
result = scheduler.create()
for r in result:
    print(r["Doctor"].id, r["Shift"].date, r["Shift"].shift)
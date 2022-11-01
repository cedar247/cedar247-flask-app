class Doctor:
    def __init__(self, id):
        self.id = id
        self.leaves = []

    def add_leave(self, leave):
        self.leaves.append(leave)

    def get_leaves(self):
        return self.leaves

    def is_a_leave(self, shiftOfSchedule):
        # check whether shift is a leave
        for leave in self.leaves:
            if leave.date.year == shiftOfSchedule.date.year and leave.date.month == shiftOfSchedule.date.month and leave.date.day == shiftOfSchedule.date.day: # leave date is equal to date of shift
                if shiftOfSchedule.shift in leave.shifts: # check whether shift is a leave shift
                    return True

        return False

            
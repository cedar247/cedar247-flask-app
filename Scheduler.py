from calendar import monthrange

class Scheduler:
    def __init__(self, doctors_details, shift_types, special_shifts, num_doctors,consecutive_shifts, year, month):
        self.doctors_details = doctors_details # doctor details first element doctor id next are date with shifts that he/she want a leave
        self.shift_types = shift_types # shift types in the respective ward
        self.special_shifts = special_shifts# special shift with number of vacation days needed
        self.num_doctors = num_doctors# number of doctors need per each shift
        self.consecutive_shifts = consecutive_shifts
        self.year = year
        self.month = int(month)

    def is_samedate(self, date1, date2):
        day1, month1, year1 = date1.split("-")
        day2, month2, year2 = date2.split("-")

        if day1 == day2 and month1 == month2 and year1 == year2:
            return True
        return False

    def is_a_leave(self, date, shift_type, leaves):
        
        # iterate through leaves and check whether shift is a leave
        for leave in leaves:
            if leave:
                if self.is_samedate(date, leave[0]): # date is same
                    if shift_type in leave[1:]: # shift is a leave
                        return True
            

        return False


    def create_schedule(self, assignment, shifts, depth):
        if depth == len(assignment): # base case
            return True

        # global doctors_details # doctor details first element doctor id next are date with shifts that he/she want a leave
        # global shift_types  # shift types in the respective ward
        # global special_shifts # special shift with number of vacation days needed
        # global num_doctors # number of doctors need per each shift
        # global num_days # number of days in the month

        doctor = self.doctors_details[depth][0] # doctor id
        leaves = self.doctors_details[depth][1:] # leaves needed
        num_shifts = len(self.shift_types) # number of shifts
        
        index_shift = 0
        while index_shift < self.num_days:
            date = shifts[index_shift][0] # date of the shifts
            allocations = shifts[index_shift][1:]

            index_shift_type = 0
            while index_shift_type < num_shifts:
                shift_type = self.shift_types[index_shift_type]
                can_allocate = True

                # check if the shift is a leave
                if self.is_a_leave(date, shift_type, leaves):
                    can_allocate = False
                    index_shift_type += 1
                    continue

                if can_allocate:

                    if shifts[index_shift][index_shift_type + 1] != -1 and  len(shifts[index_shift][index_shift_type + 1]) == self.num_doctors[shift_type]:
                        index_shift_type += 1
                        can_allocate = False
                        continue
                    if assignment[doctor] == -1:
                        assignment[doctor] = [[date, shift_type]]
                        
                        if shifts[index_shift][index_shift_type + 1] == -1:
                            shifts[index_shift][index_shift_type + 1] = [doctor]
                        else:
                            shifts[index_shift][index_shift_type + 1].append(doctor)

                    else:
                        assignment[doctor].append([date, shift_type])

                        if shifts[index_shift][index_shift_type + 1] == -1:
                            shifts[index_shift][index_shift_type + 1] = [doctor]
                        else:
                            shifts[index_shift][index_shift_type + 1].append(doctor)

                    
                    # check if shift is a special shift
                    if shift_type in self.special_shifts:
                        vacation = self.special_shifts[shift_type]
                        index_shift += vacation
                        break
                    
                    if not (shift_type in self.consecutive_shifts):
                        index_shift_type += 1
                index_shift_type += 1

            index_shift += 1

        self.create_schedule(assignment, shifts, depth + 1)

    def get_schedule(self):
        shifts = []
        assignment = {}

        first_day, self.num_days = monthrange(self.year, self.month)

        for i in range(1, self.num_days+1):
            date = str(self.year) + "-" + str(self.month) + "-" + str(i)

            shift = [date]
            for i in range(len(self.shift_types)):
                shift.append(-1)
            shifts.append(shift)

        for doctor_detail in self.doctors_details:
            assignment[doctor_detail[0]] = -1

        result = self.create_schedule(assignment, shifts, 0)

        # print(assignment)
        return shifts


if __name__ == "__main__":

    # details of doctors
    doctors_details = [
        ["1", ["2022-12-2", "morning"], ["2022-12-23", "evening", "night"]],
        ["2", ["2022-12-3", "evening"], ["2022-12-8", "morning", "night"]],
        ["3", ["2022-12-9", "night"], ["2022-12-20", "evening", "night"]],
        ["4", ["2022-12-12", "evening"], ["2022-12-18", "morning", "night"]],
        ["5", ["2022-12-7", "evening"], ["2022-12-29", "evening", "night"]],
        ["6", ["2022-12-6", "evening"], ["2022-12-18", "morning", "night"]],
        ["7", ["2022-12-29", "evening"], ["2022-12-13", "evening", "night"]],
        ["8", ["2022-12-13", "night"], ["2022-12-26", "morning", "night"]],
    ]

    shift_types = ["morning", "evening", "night"] # shift types
    consecutive_shifts = {"morning":"evening"} # consecutive shifts that can do consecutively
    special_shifts = {"night": 1} # special shift with vacation in days
    num_doctors = {"morning": 2, "evening": 3, "night": 4} # number of doctors need for each shift

    
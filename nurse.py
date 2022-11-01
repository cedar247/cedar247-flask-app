from ortools.sat.python import cp_model

# creates the data
num_nurses = 4
num_shifts = 3
num_days = 3
all_nurses = range(num_nurses)
all_shifts = range(num_shifts)
all_days = range(num_days)

# creates the model
model = cp_model.CpModel()

"""
The array defines assignments for shifts to nurses as follows:
shifts[(n, d, s)] equals 1 if shift s is assigned to nurse n on day d, and 0 otherwise.
"""
shifts = {}
for n in all_nurses:
    for d in all_days:
        for s in all_shifts:
            shifts[(n, d, s)] = model.NewBoolVar('shift_n%id%is%i' % (n, d, s))

# Assign nurses to shifts

# each shift is assigned to a single nurse per day
for d in all_days:
    for s in all_shifts:
        model.AddExactlyOne(shifts[(n, d, s)] for n in all_nurses)

# Each nurse works at most one shift per day
for n in all_nurses:
    for d in all_days:
        model.AddAtMostOne(shifts[(n, d, s)] for s in all_shifts)


from Scheduler import Scheduler 

def test_is_samedate():
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
    num_doctors = {"morning": 2, "evening": 3, "night": 4} # number of doctors
    year = 2022
    month = 12
    scheduler = Scheduler(doctors_details, shift_types, special_shifts, num_doctors, consecutive_shifts, year, month)
    assert scheduler.is_samedate("2022-12-2", "2022-12-2") == True
    assert scheduler.is_samedate("2022-12-2", "2022-12-3") == False

def test_is_a_leave():
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
    num_doctors = {"morning": 2, "evening": 3, "night": 4} # number of doctors
    year = 2022
    month = 12
    scheduler = Scheduler(doctors_details, shift_types, special_shifts, num_doctors, consecutive_shifts, year, month)
    assert scheduler.is_a_leave("2022-12-2", "morning", [["2022-12-2", "morning"], ["2022-12-23", "evening", "night"]]) == True
    assert scheduler.is_a_leave("2022-12-3", "morning", [["2022-12-2", "morning"], ["2022-12-23", "evening", "night"]]) == False

def test_get_schedule():
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
    num_doctors = {"morning": 2, "evening": 3, "night": 4} # number of doctors
    year = 2022
    month = 12
    scheduler = Scheduler(doctors_details, shift_types, special_shifts, num_doctors, consecutive_shifts, year, month)
    assert scheduler.get_schedule() != []
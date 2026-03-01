# Student marks analyser

def average_marks(marks_list):
    total_marks = 0
    total_entries = len(marks_list)
    for mark in marks_list:
        total_marks += mark
    average = total_marks / total_entries
    return average

def highest_mark(marks_list):

    high = marks_list[0]

    for mark in marks_list:
        if mark > high:
            high = mark

    return high

def passed_count(marks_list):
    count = 0
    for mark in marks_list:
        if mark > 40:
            count += 1

    return count

n = input("Enter marks separated by spaces: ")
marks_list = list(map(int, n.split()))
avg = average_marks(marks_list)
print(f"Average marks: {avg}")
high = highest_mark(marks_list)
print(f"Highest marks: {high}")
passed = passed_count(marks_list)
print(f"Passed count: {passed}")
    

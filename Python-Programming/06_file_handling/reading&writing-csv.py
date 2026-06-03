import csv

# For seperate values like this use .writerow()

with open("Sample.csv", "w", newline="") as file: # newline="" prevents blank lines on windows
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age'])
    writer.writerow(['Nibras', 18])
    writer.writerow(['Mohamed', 25])

# For whole values like this use .writerows()

rows = [
    
    ['Harry', 18],
    ['Sophie', 18]
]

with open("Sample.csv", "a", newline="") as file: 
    writer = csv.writer(file)
    writer.writerows(rows)
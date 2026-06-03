
# List inside a dictionary 

student = {
    "Name" : "Nibras",
    "Marks" : [100, 99, 99]
}

print(student["Marks"][0])

# Dictionary inside a dictionary 

student1 = {

    "name" : "Nibras",
    "Marks" : {
        "Phy" : 90
    }
}

print(student1["Marks"]["Phy"])

# Dictionary inside a list

student2 = [
    {
        "Phy" : 90
    }
]

print(student2[0])
# Title

import shutil
width = shutil.get_terminal_size().columns
print("=" * width)
print("EXPENSE TRACKER 📊".center(width))
print("=" * width)

# Menu
expenses = [ ]

# Adding back data to list after restarting
try:
    with open("expenses.txt", "r") as file:
        for line in file:
            line = line.strip()

            if line:
                amount, category, description = line.split(",")
                expenses.append((amount, category, description))

except FileNotFoundError:
    pass


while True:
    print("\n1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Spent")
    print("4. Exit")

    # Choosing choice
    while True:
        choice = input("\nChoose an option: ")
        if choice in ("1", "2", "3", "4"):
            print("Your choice: ", choice)
            break

        else:
            print("Invalid Choice❌...Choose 1, 2, 3, or 4")
        

    # Menu logic

    if choice == "1":
        print("Add Expense SELECTED ✅\n")
        while True:
            amount = input("Enter the Amount: ")
        
            try:
                float(amount)
                break
            except ValueError:
                print("Invalid Amount ❌...Enter valid amount")

        category = input("Enter Category: ")
        description = input("Enter the Description: ")
        expenses.append((amount, category, description))
        print(f"\nExpense Added -> Amount: {amount} | Category: {category} | Description: {description} ")

        with open("expenses.txt", "a") as file:
            file.write(f"{amount},{category},{description} \n")
        

    elif choice == "2":
        print("View All Expenses SELECTED ✅")
        if not expenses:
            print("No expenses added yet ! ")

        else: 
            for amount, category, description in expenses:
                print(f"\nExpenses -> Amount: {amount} | Category: {category} | Description: {description} ")

    elif choice == "3":
        print("View Total Spent SELECTED ✅")
        total = 0
        if not expenses:
            print("No expenses added yet ! ")

        else:
            for amount, category, description in expenses:
                total += float(amount)
        print(f"\nTotal Amount Spent: INR. {total}")

    elif choice == "4":
        print("Exiting....⌛")
        break

    else:
        print("Invalid choice ❌ ")
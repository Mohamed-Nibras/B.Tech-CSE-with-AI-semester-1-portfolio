# Title

import shutil
width = shutil.get_terminal_size().columns
print("=" * width)
print("EXPENSE TRACKER 📊".center(width))
print("=" * width)

from datetime import date


# Adding back data to list after restarting
def load_expenses():
    expenses = []
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                line = line.strip()

                if line:
                    dat_val, amount, category, description = line.split(",")
                    expenses.append((dat_val, amount, category, description))

    except FileNotFoundError:
        pass

    return expenses


def get_valid_choice():
        while True:
            choice = input("\nChoose an option: ")
            if choice in ("1", "2", "3", "4"):
                print("Your choice: ", choice)
                return choice

            else:
                print("Invalid Choice❌...Choose 1, 2, 3, or 4")


def add_expense(expenses):
    
        print("Add Expense SELECTED ✅\n")
        today = date.today().isoformat()
        while True:
            amount = input("Enter the Amount: ")
        
            try:
                float(amount)
                break
            except ValueError:
                print("Invalid Amount ❌...Enter valid amount")

        category = input("Enter Category: ")
        description = input("Enter the Description: ")
        expenses.append((today, amount, category, description))
        print(f"\nExpense Added -> Date: {today} | Amount: {amount} | Category: {category} | Description: {description} ")

        with open("expenses.txt", "a") as file:
            file.write(f"{today},{amount},{category},{description}\n")

def view_expenses(expenses):
    
        print("View All Expenses SELECTED ✅")
        if not expenses:
            print("No expenses added yet ! ")

        else: 
            for date, amount, category, description in expenses:
                print(f"\nExpenses -> Date: {date} | Amount: {amount} | Category: {category} | Description: {description} ")

def view_total_spent(expenses):
     
        print("View Total Spent SELECTED ✅")
        total = 0
        if not expenses:
            print("No expenses added yet ! ")

        else:
            for _, amount, _, _ in expenses:
                total += float(amount)
        print(f"\nTotal Amount Spent: INR. {total}")

expenses = load_expenses()
while True:
    print("\n1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Spent")
    print("4. Exit")

    
    choice = get_valid_choice()

    if choice =="1":
        add_expense(expenses)

    elif choice == "2":
        view_expenses(expenses)

    elif choice == "3":
         view_total_spent(expenses)    

    

    elif choice == "4":
        print("Exiting....⌛")
        break

    else:
        print("Invalid choice ❌ ")
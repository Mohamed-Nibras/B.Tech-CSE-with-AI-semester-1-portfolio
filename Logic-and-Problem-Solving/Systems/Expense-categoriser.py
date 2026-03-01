# Expense categorizer

def categorize_expense():
    n = int(input("Enter the number of expenses: "))

    category_totals = {}
    for i in range(n):
        category = input(f"Enter the category for expense {i + 1}: ")
        amount = input(f"Enter the amount for expense {i + 1}: ")
        amount = float(amount)

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount
    print("\nExpense Summary:")
    for category, total in category_totals.items():
        print(f"{category}: ${total:.2f}")
categorize_expense()


try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("ERROR: Age should be positive")
    income = 2000000
    risk = income/age
    print(age)

except (ValueError, ZeroDivisionError):
    print("Age must be a number, and greater than zero")

# Alternate except method for covering all errors in one block

except Exception as e:
    print("Your error:", e)

finally: # No matter what this will run
    print("This block will be interpretated no matter if you have or don't have an error")


# Title
import shutil
width = shutil.get_terminal_size().columns
print("=" * width)
print("USER RISK CALCULATOR".center(width))
print("=" * width)

def user_input():
    try:
        data = {
            'Age' : int(input("Enter your age: ")),
            'Income' : int(input("Enter your income: "))
        }
        if data["Age"] <= 0 or data["Income"] <= 0:
            raise ValueError("Age and Income should be greater than zero ! ")
        
        
        return data
        
    except ValueError as e:
        print("Error: ", e)
        return None
    
    except Exception as e:
        print("Unexpected error:", e)
        return None
    
    finally:
        print("Program execution completed")


    

def risk_calculation(data):
    risk = data['Income'] / data['Age']
    return risk

def final_output(data, risk):
    print(f"AGE: {data['Age']}")
    print(f"INCOME: {data['Income']}")
    print(f"RISK: {risk:.2f}")


data = user_input()

if data is not None:
    risk = risk_calculation(data)
    final_output(data, risk)


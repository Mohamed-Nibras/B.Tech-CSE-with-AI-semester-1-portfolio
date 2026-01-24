"""
Logic Solver App - Mini Project (Semester 1)

Contains:
1. Number Guessing Game
2. Math Quiz
3. Number Puzzle
4. Persistent score storage using file handling

Concepts used:
- Functions
- Loops
- Conditionals
- Random module
- File handling
- Input validation
- Modular design

Author: Mohamed Nibras
"""

import random
import shutil
width = shutil.get_terminal_size().columns

# Save scores

def save_scores(scores):
      with open("scores.txt", "w") as file:
            for game, score in scores.items():
                  file.write(f"{game} : {score}\n")

# Load scores

def load_scores():
      scores = {
    "number_guessing": 0,
    "math_quiz": 0,
    "number_puzzle": 0
      }
      try:
            with open("scores.txt", "r") as file:
                  for line in file:
                        game, score = line.strip().split(" : ")
                        scores[game] = int(score)
      except FileNotFoundError:
            pass
      
      return scores

# Number guessing game

def number_guessing():
    print("\n" + "="*width)
    print("NUMBER GUESSING GAME 🔢".center(width))
    print("="*width)
    
    secret_number = random.randint(1, 30)
    attempts = 5
    final_score = 0
    while attempts > 0:
        try:
            guess = input("\nEnter your guess ( 1 to 30 ): ").strip()
            if not guess.isdigit():
                raise ValueError("Please enter a valid number.")
            guess = int(guess)
            print(f"Your guess: {guess}")
        except(ValueError):
                print("Enter a valid number")
                continue

        if guess == secret_number:
                print(f"\nYou guessed it correctly ✅")
                print(f"Secret number -> {secret_number}")
                print(f"Your number -> {guess}")
                score = attempts 
                print(f"Your score is: {score}")
                final_score = score
                break
        elif guess < secret_number:
                print(f"Try bigger than {guess}")
        elif guess > secret_number:
                print(f"Try smaller than {guess}")

        attempts -= 1
        print(f"\nYou have {attempts} attempts left")
        

    if attempts == 0:
        print(f"You've used all attempts ⚠️. The secret number was {secret_number}.")
    print(f"\nYour final score is: {final_score}/5")
    input("Press Enter to return to menu...")
    print("\nReturning to menu...✅\n")

    return final_score

# Math quiz game

def math_quiz():
      print("\n" + '='*width)
      print("MATH QUIZ 📃".center(width))
      print("="*width)
      final_score = 0
      asked = set()
      for i in range(1, 6):
            while True:
                        
                a = random.randint(1, 20)
                b = random.randint(1, 20)
                op = random.choice(["+", "-", "*", "/"])

                question = (a, op, b)
                if question not in asked:
                    asked.add(question)
                    break
            
            if op == "+":
                    answer = a + b
            elif op == "-":
                    answer = a - b
            elif op == "*":
                    answer = a * b
            else:
                    answer = round(a / b, 2)

            print(f"\nQuestion {i}: {a} {op} {b}?")
            while True:
                try:
                    user_input = float(input("Enter your answer: "))
                    break
                except ValueError:
                    print("Invalid number ❌")

            if abs(user_input - answer) < 0.01:
                  print("Correct ✅")
                  final_score += 1
            else:
                  print(f"Wrong ❌ The correct answer is {answer}")

      print(f"\nYour final score is: {final_score}/5")
      input("Press Enter to return to menu...")
      print("\nReturning to menu...✅\n")

      return final_score

# Number puzzle game

def number_puzzle():
      print("\n" + '='*width)
      print("NUMBER PUZZLE 🧩".center(width))
      print("="*width)
      final_score = 0

      for q in range(1, 6):
            pattern = random.choice(["add", "mul", "square"])
            start = random.randint(1, 20)

            if pattern == "add":
                  step = random.randint(1, 10)
                  puzzle = [ start + step * i for i in range(5)]
            elif pattern == "mul":
                  step = random.randint(1, 10)
                  puzzle = [ start * (i + 1) for i in range(5)]
            elif pattern == "square":
                  puzzle = [ (start + i)**2 for i in range(5)]

            print(f"\nQuestion {q}: {', '.join(map(str, puzzle[:4]))} , __")
            while True:
                try:
                    user_input = int(input("Enter the missing number: "))
                    break
                except ValueError:
                    print("Invalid number ❌")

            if user_input == puzzle[4]:
                  print("Correct ✅")
                  final_score += 1
            else:
                  print(f"Wrong ❌ The correct answer is {puzzle[4]}")
      print(f"\nYour final score is: {final_score}/5")
      input("Press Enter to return to menu...")
      print("\nReturning to menu...✅\n")

      return final_score

# Show menu 

def show_menu():
    print("="*width)
    print(" " * ((width // 2) - 7) + "GAME MENU")
    print("="*width)
    print("1. Number Guessing Game")
    print("2. Math Quiz Game")
    print('3. Number puzzle game')
    print("4. View Scores")
    print("5. Reset Scores")
    print("6. Help")
    print("7. Exit")
    print("="*width)

# Show scores

def view_scores(scores):
    print("\n" + "="*width)
    print(" " * ((width // 2) - 6) + "SCORES")
    print("="*width)
    print(f"Number Guessing Game Score: {scores['number_guessing']}")
    print(f"Math Quiz Game Score: {scores['math_quiz']}")
    print(f"Number Puzzle Game Score: {scores['number_puzzle']}")
    print("="*width + "\n")
    input("Press Enter to return to menu...")
    print("\nReturning to menu...✅\n")


# Reset scores

def reset_scores(scores):
    for key in scores:
        scores[key] = 0

    print("\n✅ Scores have been reset.\n")
    input("Press Enter to return to menu...")
    print("\nReturning to menu...✅\n")


# Help

def show_help():
    print("\n" + "="*width)
    print(" " * ((width // 2) - 4) + "HELP")
    print("="*width)
    print("1. Number Guessing Game: Guess a number between 1 and 30.")
    print("2. Math Quiz Game: Solve math problems.")
    print("3. Number Puzzle Game: Solve number puzzles.")
    print("4. View Scores: See your scores for each game.")
    print("5. Reset Scores: Reset all scores to zero.")
    print("6. Help: Show this help menu.")
    print("7. Exit: Quit the game.")
    print("="*width + "\n")
    input("Press Enter to return to menu...")
    print("\nReturning to menu...✅\n")


# Main loop

def main():
      scores = load_scores()
      while True:
            show_menu()
            choice = input("\nEnter your operation: ")

            if choice == '1':
                  scores["number_guessing"] = number_guessing()
                  save_scores(scores)
            elif choice == '2':
                  scores["math_quiz"] = math_quiz()
                  save_scores(scores)
            elif choice == '3':
                  scores["number_puzzle"] = number_puzzle()
                  save_scores(scores) 
            elif choice == '4':
                  view_scores(scores)
            elif choice == '5':
                  reset_scores(scores)
                  save_scores(scores)
            elif choice == '6':
                  show_help()
            elif choice == '7':
                  print("Exiting the game. Goodbye 👋🏻")
                  break
            else:
                  print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
      main()
# Palindrome Checker

# Reversing the word



def is_palindrome(string):
    cleaned = ''.join(string.split()).lower()
    reversed = ""
    for ch in cleaned:
        reversed = ch + reversed
    return reversed == cleaned

string = input("Enter a string: ").strip()
result = is_palindrome(string)
if result:
    print(f"The string is a palindrome {string}.")
else:
    print(f"The string is not a palindrome {string}")
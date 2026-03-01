# Anagram checker

def anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    if len(str1) != len(str2):
        return False
    
    char_count = {}
    
    for ch in str1:
        char_count[ch] = char_count.get(ch, 0) + 1
    
    for ch in str2:
        if ch in char_count:
            char_count[ch] -= 1
            if char_count[ch] < 0:
                return False
        else:
            return False
    
    return True

input_str1 = input("Enter the first string: ")
input_str2 = input("Enter the second string: ")
if anagram(input_str1, input_str2):
    print(f'"{input_str1}" and "{input_str2}" are anagrams.')
else:
    print(f'"{input_str1}" and "{input_str2}" are not anagrams.')

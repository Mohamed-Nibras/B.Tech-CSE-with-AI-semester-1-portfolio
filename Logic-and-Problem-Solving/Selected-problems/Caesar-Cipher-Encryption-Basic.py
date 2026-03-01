# Caesar Cipher Encryption Basic

def caesar_cipher_encrypt(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            shiftbase = ord('A') if char.isupper() else ord('a')
            # shiftbase = ord('A') if char.isupper() else ord('a') gives the ASCII value of 'A' or 'a' based on case
            encrypted_char = chr((ord(char) - shiftbase + shift) % 26 + shiftbase)
            # ord(char) - shiftbase gets the 0-25 index of the letter (position of alphabet)
            # % 26 ensures it repeats after 'z' or 'Z'
            # + shiftbase converts it back to ASCII after finding the new postion
            encrypted_text += encrypted_char
        else: 
            encrypted_text += char
    
    return encrypted_text

plaintext = input("Enter the plaintext: ")
shift1 = int(input("Enter the shift value: "))
encrypted_text = caesar_cipher_encrypt(plaintext, shift1)
print("Encrypted text:", encrypted_text)

# Method 2 using list

def encryption(text, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for ch in text.lower():
        if ch in alphabet:
            index = alphabet.index(ch)
            new_index = (index + shift) % 26
            result += alphabet[new_index]
        else:
            result += ch
    
    return result

text = input("Enter the plaintext: ")
shift2 = int(input("Enter the shift value: "))
encrypted_text = encryption(text, shift2)
print("Encrypted text:", encrypted_text)
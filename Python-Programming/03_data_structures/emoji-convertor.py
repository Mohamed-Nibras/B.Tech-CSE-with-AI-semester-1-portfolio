
text = input("-->  ")
words = text.split(" ") # Splits the words into lists when it reaches the given character, in this case it is space 
emoji = {
    ":)" : "😁",
    ":(" : "😔"
}
output = ""
for x in words:
    output += emoji.get(x, x) + " "
print(output) 
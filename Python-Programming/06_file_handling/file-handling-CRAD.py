import os

# r - Read
# a - Append
# w - Write
# x - Create


# 1. Reading a file - Display: Error if the file doesn't exist

file = open("names.txt")
print(file.read()) # Reads the entire file fully
print(file.read(4)) # Reads the first 4 characters of the file, to read again we must reopen or use file.seek(index)

print(file.readline()) # Reads the first line from current cursir positiona and automatically goes to next in next readline
print(file.readline()) # Reads consecutive lines if mentioned twice

for line in file:
    print(line) # Reads line in loop similar to readline function, more easy to use


file.close() # We close a file to ensure all buffered data is written to disk and to free system resources.


# 2. Appending files - Adding 2 files, and it creates the file if it doen't exist

file = open("names.txt", "a") #  "a" is to tell the function that we are appending
file.write("Nibu\n") # Appends this name to the file that has been called
file.close()

file = open("names.txt")
print(file.read()) # Called to read the new file after appending
file.close()

# ALTERNATE METHOD FOR BETTER AND REAL WORLD PROGRAMMER LEVEL, ie. Using keyword 'With'

with open("names.txt", "a") as file:
    file.write("Nibu\n")
    # Because it automatically closes the file, safer and cleaner, used in real projects & interviews


# 3. Write (Overwrite) - Overwrites the mentioned file, works the same way as append in terms file searching
file = open("context.txt", "w") #  "w" is to tell the function that we are overwriting
file.write("The content is overwritten") # overwrites the file that has been called
file.close()

file = open("context.txt")
print(file.read()) # Called to read the new file after overwriting
file.close()


# 4. Creating files - 2 ways 

# WAY 1 - Creating using write method, creates the file if it doesn't exist, opens it if it does

file = open("New file 1.txt", "w") # Creates this fie since it doesn't exist for the first time
file.close()

# WAY 2 - Using the create method, creates the specifies file, but returns an error if it already exists

file = open("New file 2.txt", "x")
file.close()

# To check if a file exists or not

# Import os first

if not  os.path.exists("New file 3.txt"):
    file = open("New file 3.txt", "x")
    file.close()


# Delete a file - By checking in the os file try, also use conditional logic to avoid errors

if os.path.exists("New file 1.txt"):
    os.remove("New file 1.txt")
else:
    print("The file doesn't exist ")

# For deleting multiple files at once, we can add those files in a list and use loops to run through out those files and can delete it
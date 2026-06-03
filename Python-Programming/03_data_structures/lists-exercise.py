# To find the greatest number in a list 

number = [ 100, 67, 43, 78, 88, 56 ]
greatestnum = number[2]

for i in number:
    if i > greatestnum:
        greatestnum = i
print(greatestnum)

# To remove the duplicate in numbers list (using list methods)

num = [2, 2, 3, 4, 5, 5, 3, 1, 0]
num_without_duplicate = []

for x in num:
    if x not in num_without_duplicate:
        num_without_duplicate.append(x)

print(num_without_duplicate)
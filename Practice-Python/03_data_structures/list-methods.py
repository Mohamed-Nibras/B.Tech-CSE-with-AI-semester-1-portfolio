#Append --> adds value at the end
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)

#Insert --> insert values at specific places
x = [1, 2, 3, 4, 5]
x.insert(1, 10)
print(x)

#Remove --> removes value
y = [1, 2, 3, 4, 5]
y.remove(1)
print(y)

#Clear --> clears whole list
z = [1, 2, 3, 4, 5]
z.clear()
print(z)

#Pop --> removes last element of the list
q = [1, 2, 3, 4, 5]
q.pop()
print(q)

#Index --> to check the index of the existing element
e = [1, 2, 3, 4, 5]
print(e.index(5))
#Another method (safer without errors)
e = [1, 2, 3, 4, 5]
print(5 in e)

#Count --> count the number of repeated elements in the list
p = [1, 2, 3, 4, 5, 5]
print(p.count(5))

#Sort --> sorts variable in order
o = [5, 3, 2, 4, 1]
o.sort()
print(o)

#Reverse --> reverses the order
o = [5, 3, 2, 4, 1]
o.sort()
o.reverse()
print(o)

#Copy --> copies the list in to another variable, but changing in the original set will not change the copy
L= [1, 2, 3, 4, 5]
copy = L.copy()
L.append(6)
print(copy)
# disjoint set 
s1 = {1,2,3,4,5}
s2 = {6,7,8,9,}

print(s1.isdisjoint(s2))

# superset 
set1 = {1,2,3,4}
set2 = {1,2,3,4}

print(set1.issuperset(set2))

# subset 
w1 = {1,2,3,4}
w2 = {2,4}

print(w2.issubset(w1))

# add
city1 = {'mad' ,'che' ,'mum'}
city1.add('hyd')
print(city1)

# remove or discard 
q1 = {1,2,3,4}
q1.remove(2)
q1.remove(3)
print(q1)

# pop
e = {1,2,3,4,5}
item = e.pop()
print(e)
print(item)



# clear 
r = {1,2,3,4}
r.clear()
print(r)

# check if item exists 
u = {1,2,3,4}
if 1 in u :
    print(u)
else :
    print('u is absent ')
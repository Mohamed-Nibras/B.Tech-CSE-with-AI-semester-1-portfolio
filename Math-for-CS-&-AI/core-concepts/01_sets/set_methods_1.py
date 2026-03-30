# for union and update:

city1 = {"Chennai" ,"Bangalore" ,"Hyderabad" }
city2 = {"Delhi" ,"Mumbai" ,"Chennai" ,"Ahmedabad" }
city1.update(city2)
print(city1.union(city2))
print(city1)


# for intersection and update , and symmetric difference and difference and difference update:


s1 = {1,2,3}
s2 = {2,3,4,5}



s1.intersection_update(s2)
print(s1)

# example for all 
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

print(s1.union(s2))                     # {1,2,3,4,5,6}
print(s1.intersection(s2))              # {3,4}
print(s1.difference(s2))                # {1,2}
print(s1.symmetric_difference(s2))      # {1,2,5,6}

s1.update(s2)                            # s1 becomes {1,2,3,4,5,6}
s1.intersection_update(s2)               # s1 becomes {3,4,5,6} 
s1.difference_update(s2)                 # s1 becomes elements not in s2
s1.symmetric_difference_update(s2)       # s1 becomes all non-common elements













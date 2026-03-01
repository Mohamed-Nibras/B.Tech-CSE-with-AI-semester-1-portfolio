#number square 1 1 1 1
#              2 2 2 2 
for i in range(4):
    for j in range(4):
        print(i + 1, end =" ")

    print('\n')

#number square 1 2 3 4
#              1 2 3 4
for i in range(4):
    for j in range(4):
        print(j + 1, end =" ")

    print('\n')

#number triangle
# 1
# 2 2
# 3 3 3 
for i in range(4):
    for j in range(i + 1):
        print(i + 1, end = " ")

    print('\n')

#number triangle
# 1
# 1 2
# 1 2 3
for i in range(4):
    for j in range(i + 1 ):
        print(j + 1, end = " ")

    print('\n')

# number pyramid
#    1
#  2    2
# 3  3   3
rows = 5
for i in range(1,rows + 1):
  print(" " * (rows - i), end = " " ) 
  for j in range(1, i + 1):
      print(i, end = " ")
  print('\n')

# number pyramid
#    1
#  1   2
# 1  2  3
rows = 5
for i in range(1,rows + 1):
  print(" " * (rows - i), end = " " ) 
  for j in range(1, i + 1):
      print(j, end = " ")
  print('\n')  

# inverse number pyramid
# 3  3   3
#  2   2
#    1
rows = 5
for i in range(rows, 0, -1):
  print(" " * (rows - i), end = " " ) 
  for j in range(1, i + 1):
      print(i, end = " ")
  print('\n')

# inverse number pyramid
# 1  2  2
#  1   2
#    1
rows = 5
for i in range(rows, 0, -1):
  print(" " * (rows - i), end = " " ) 
  for j in range(1, i + 1):
      print(j, end = " ")
  print('\n')
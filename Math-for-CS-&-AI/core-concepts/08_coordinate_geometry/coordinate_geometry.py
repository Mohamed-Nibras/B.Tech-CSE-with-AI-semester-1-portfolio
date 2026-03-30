import matplotlib.pyplot as plt

x1, y1 = 2, 3
x2, y2 = 4, 5
x3, y3 = 6, 7

# Line A → B
plt.plot([x1, x2], [y1, y2], marker='o')

# Line B → C
plt.plot([x2, x3], [y2, y3], marker='o') # Matches with index

plt.text(x1, y1, 'A')
plt.text(x2, y2, 'B')
plt.text(x3, y3, 'C')

plt.title("THREE COORDINATES CONNECTED")
plt.grid()

plt.show()
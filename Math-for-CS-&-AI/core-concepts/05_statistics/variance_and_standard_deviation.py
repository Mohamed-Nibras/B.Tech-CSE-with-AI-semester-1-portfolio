def mean(data):
    return sum(data) / len(data)

def variance(data):
    m = mean(data)
    squared_diff_sum = 0

    for x in data:
        squared_diff_sum += (x - m) ** 2

    return squared_diff_sum / len(data)

def standard_deviation(data):
    return variance(data) ** 0.5


data = [10, 20, 30]

print(round(mean(data), 3))
print(round(variance(data), 3))
print(round(standard_deviation(data), 3))
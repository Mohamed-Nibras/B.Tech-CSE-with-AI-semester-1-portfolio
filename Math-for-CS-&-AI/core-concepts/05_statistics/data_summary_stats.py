# Finding mean, median, mode

def find_mean(data):
    total = 0
    for i in data:
        total += i
    number = len(data)
    mean = total / number

    return round(mean, 3)

def find_median(data):
    
    data = sorted(data)
    n = len(data)
    if n % 2 == 0:
        return (data[n // 2 - 1] + data[n // 2]) / 2
    else:
        return data[n // 2]

def find_mode(data):
    frequency = {}
    for num in data:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values())

    mode = [num for num, freq in frequency.items() if freq == max_freq]
    if max_freq == 1:
        return "No mode"
    elif len(mode) == 1:
        return mode[0]
    else:
        return mode

def main():
    print("=== DATA SUMMARY ===")   
    print("Mean =",find_mean([1,2,3,3,4,4,5]))
    print("Median =",find_median([1,2,3,3,4,4,5]))
    print("Mode =",find_mode([1,2,3,4,4,5]))

main()
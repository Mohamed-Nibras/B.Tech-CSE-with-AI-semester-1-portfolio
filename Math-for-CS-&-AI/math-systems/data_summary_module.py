import statistics as stats

def user_input():
    user_input = input("Enter numbers (separated by commas): ")
    try:
        data = [float(num.strip()) for num in user_input.split(",")]
        return data
    except ValueError:
        print("Invalid input ❌")
        return None

def find_mean(data):
    return round(sum(data) / len(data), 3)

def find_median(data):
    data = sorted(data)
    n = len(data)
    if n % 2 == 0:
        return (data[n//2 - 1] + data[n//2]) / 2
    else:
        return data[n//2]

def find_mode(data):
    frequency = {}
    for num in data:
        frequency[num] = frequency.get(num, 0) + 1

    max_freq = max(frequency.values())
    modes = [num for num, freq in frequency.items() if freq == max_freq]

    if max_freq == 1:
        return None
    elif len(modes) == 1:
        return modes[0]
    else:
        return modes

def main():
    data = user_input()
    if data is None:
        return

    print("\n=== DATA SUMMARY ===")
    print("Data:", data)

    print("\n--- Manual ---")
    print("Mean:", find_mean(data))
    print("Median:", find_median(data))
    print("Mode:", find_mode(data))

    print("\n--- Using statistics module ---")
    print("Mean:", stats.mean(data))
    print("Median:", stats.median(data))
    print("Mode:", stats.multimode(data))
    print("Standard Deviation:", round(stats.stdev(data), 3))

main()


# Word frequency toolkit

import string

def text_clean(text):
    lower_text = text.lower()

    for i in string.punctuation:
        lower_text = lower_text.replace(i, "")
    return lower_text

def word_frequency(clean_text):
    freq_word = {}
    words = clean_text.split()

    for ch in words:
        freq_word[ch] = freq_word.get(ch, 0) + 1
    return freq_word

def most_freq(freq_dict):
    max_count = 0
    max_word = None

    for word, count in freq_dict.items():
        if count > max_count:
            max_count = count
            max_word = word
    return max_word, max_count

def histogram(freq_dict):
    for word, count in freq_dict.items():
        print(f"{word}: {'*' * count}")
    

input_text = input("Enter a string: ").strip()
if not input_text:
    print("No input provided")
    exit()
cleaned_text = text_clean(input_text)

frequency_table = word_frequency(cleaned_text)

print("\nFrequency table")
for w, c in frequency_table.items():
    print(f"{w}: {c}")

most_repeated_word, most_count = most_freq(frequency_table)
print(f"Most repeated word: {most_repeated_word}, and it is repeated {most_count} times.")

histo_print = histogram(frequency_table)
        
sorted_freq = sorted(frequency_table.items())
print("\nSorted frequency table")
for w, c in sorted_freq:
    print(f"{w}: {c}")


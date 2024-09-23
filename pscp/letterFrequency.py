"""Letter Frequency"""
def freq(txt):
    """Find the most frequent letter"""
    freq_dict = {}
    for letter in txt:
        if letter.isalpha():
            freq_dict[letter] = freq_dict.get(letter, 0) + 1
    most_value_index = list(freq_dict.values()).index(max(freq_dict.values()))
    most_letter = list(freq_dict.keys())[most_value_index]
    print(most_letter)
freq(input().lower())

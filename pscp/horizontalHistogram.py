"""Horizontal Histogram"""
def horizontal_histogram(txt):
    """create a horizontal histogram"""
    histo_dict = {}
    for letter in txt:
        histo_dict[letter] = histo_dict.get(letter, 0) + 1
    histo_dict = dict(sorted(histo_dict.items(), key=lambda x: (x[0].isupper(), x[0])))
    for key, value in histo_dict.items():
        print(key, ": ", end="")
        for number in range(1, value+1):
            if number == value:
                print("-", end="")
            elif not number % 5:
                print("-|", end="")
            else:
                print("-", end="")
        print()
horizontal_histogram(input())

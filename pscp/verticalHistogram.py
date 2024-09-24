"""Vertical Histogram"""
def vert_histogram(txt):
    """create a vertical histogram"""
    text_dict = {}
    for letter in txt:
        if letter.isalpha():
            text_dict[letter] = text_dict.get(letter, 0) + 1
    text_dict = dict(sorted(text_dict.items()))
    most = max(text_dict.values())
    for num in range(most, 0, -1):
        print(f"{num:>2}", end="  ")
        for value in text_dict.values():
            if value >= num:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    print("    ", end="")
    for letter in text_dict:
        print(letter, end=" ")
vert_histogram(input())

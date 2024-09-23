"""Easy Historgram No Dict"""
def sorter(char):
    """Sorting"""
    return char.lower(), char.isupper()
def histogram(txt):
    """Create that histogram"""
    empty = ""
    for letter in txt:
        if not letter in empty and letter.isalpha():
            empty += letter
    empty = list(empty)
    empty.sort(key=sorter)
    for letter in empty:
        print(f"{letter} = {txt.count(letter)}")
histogram(input())

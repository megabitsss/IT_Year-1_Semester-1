"""Easy Historgram"""
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
    my_dict = {}
    for letter in empty:
        cnt = 0
        for sub_txt in txt:
            if sub_txt == letter:
                cnt += 1
        print(f"{letter} = {cnt}")
histogram(input())

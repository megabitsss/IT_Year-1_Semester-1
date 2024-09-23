"""Breach The Door"""
def paragraph_seperator(txt):
    """Seperate the word that is greater than six from the paragraph"""
    new_txt = ""
    for char in txt:
        if char.isalpha() or char == " ":
            new_txt += char
    my_list = new_txt.split()
    for item in my_list:
        if len(item) > 6:
            print(item, end=" ")
paragraph_seperator(input())

"""Backward"""
def reverser():
    """print each element in the list in a reverse order"""
    txt = ""
    my_list = []
    while txt != "NULL":
        txt = input()
        if txt != "NULL":
            my_list.append(txt)
    for item in my_list[::-1]:
        print(item)
reverser()

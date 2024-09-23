"""Word Sequence I"""
def sequence(txt):
    """Create a word sequence"""
    txt_len = len(txt)
    for index in range(1, txt_len+1):
        print(txt[:index])
sequence(input())

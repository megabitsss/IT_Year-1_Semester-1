"""Word Sequence II"""
def word_seq(default, target):
    """Create a word sequence from default word to target word"""
    if len(target) >= len(default):
        length = len(target) + 1
    else: #target < default; default > target
        length = len(default) + 1
    for num in range(length):
        temp = ""
        temp += target[:num] + default[num:]
        print(temp)
word_seq(input(), input())

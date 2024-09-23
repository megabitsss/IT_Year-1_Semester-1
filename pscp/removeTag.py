"""Remove Tag"""
def tag_remover(txt):
    """Remove the tag and return the actual text"""
    while "<" in txt or ">" in txt:
        index_1 = txt.index("<")
        index_2 = txt.index(">") + 1
        txt = txt.replace(txt[index_1:index_2], " ")
    print(txt.split())
tag_remover(input())

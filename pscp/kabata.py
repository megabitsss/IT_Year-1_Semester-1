"""kabata"""
def kabata_replacer(txt):
    """checker is the word is in kabata language"""
    txt = txt.replace("baka", " ") #space means error
    txt = txt.replace("bakka", "")
    txt = txt.replace("ba", "")
    txt = txt.replace("ka", "")
    txt = txt.replace("ta", "")
    if not txt:
        return "yes"
    return "no"
def main(n):
    """check no/yes"""
    for _ in range(n):
        print(kabata_replacer(input()))
main(int(input()))

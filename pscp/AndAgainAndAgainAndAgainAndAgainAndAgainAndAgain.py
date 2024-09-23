"""AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain"""
def vowel_counter(txt: str) -> int:
    """count amount of vowel in the text and return it back"""
    txt = txt.lower()
    cnt = 0
    cnt += txt.count("a")
    cnt += txt.count("e")
    cnt += txt.count("i")
    cnt += txt.count("o")
    cnt += txt.count("u")
    return cnt
def text_to_list(txt: str):
    """convert from text to list and return to another function"""
    txt = txt.replace(".", "")
    my_list = txt.split()
    sorted_list = []
    vowel = False
    for item in my_list:
        cnt = vowel_counter(item)
        if cnt >= 2:
            vowel = True
            sorted_list.append(item)
    sorted_list.sort()
    if not vowel:
        print("Nope")
    else:
        for item in sorted_list:
            print(item)
text_to_list(input())

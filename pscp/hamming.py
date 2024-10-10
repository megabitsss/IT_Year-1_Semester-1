"""Hamming"""
def hamming_distance(txt1, txt2):
    """find hamming distance"""
    cnt = 0
    for char1, char2 in zip(txt1, txt2):
        if not char1 == char2:
            cnt += 1
    print(cnt)
hamming_distance(input(), input())

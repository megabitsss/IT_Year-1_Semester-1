"""Blackjack"""
def blackjack_finder(num):
    """find the best possibly score of the user"""
    sigma = 0
    ace_cnt = 0
    for _ in range(num):
        card = input()
        if card.isnumeric(): #is number
            sigma += int(card)
        else: #is J, Q, K, A
            if card == "A": #pass the ace addition
                ace_cnt += 1 #นับไว้ว่ามีกี่ใบ
                sigma += 11 #บวก 11 ไปก่อน
            else: #J, Q, K
                sigma += 10
    for _ in range(ace_cnt):
        if sigma > 21:
            sigma -= 10 #equivalent to changing from A(+11) to A(+1) -> -11 + 1
        else:
            break
    print(sigma)
blackjack_finder(int(input()))
#A, 10, J
#A, A, K****
#key ผลรวมของอะไรก็ตามที่ไม่ใช่ Ace ต้องบวกก่อน เพราะมีแค่ Ace ที่เปลี่ยนค่าได้
#key ต้องดูไพ่ทั้ง 3 ใบก่อนค่อยวิเคราะห์, Ace is the problem
#key คะแนนที่ดีทีสุดที่เป็นไปได้ ใน 3 ใบ (Possibilities!)

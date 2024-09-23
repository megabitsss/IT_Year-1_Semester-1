'''stamps'''
def stamp():
    '''donut again and again'''
    n = int(input())
    stamp_total = 0
    cash = 0
    a,b,c,d = int(input()),int(input()),int(input()),int(input())
    for _ in range(n):
        bill = int(input())
        if stamp_total >= c:
            while stamp_total >= c:
                stamp_total -= c
                bill -= d
                if bill < 0:
                    bill = 0
            cash += bill
        else:
            cash += bill
        if bill >= a:
            stamp_total += (bill//a)*b
    print(cash,stamp_total,sep='\n')
stamp()

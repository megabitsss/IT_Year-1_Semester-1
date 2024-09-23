"""sequence xii"""
def pattern(n):
    """create an patter"""
    for row in range(-n+1, n):
        for column in range(-n+1, n):
            k = n - abs(abs(row) - abs(column))
            print(f"{k:02d}", end=" ")
        print()
pattern(int(input()))

"""Missing Number"""
def missing_finder(n):
    """Find the missing number"""
    all_number = set()
    my_set = set()
    for num in range(1, n+1):
        all_number.add(num)
    while True:
        number = int(input())
        if not number:
            break
        my_set.add(number)
    for number in sorted(all_number - my_set):
        print(number)
missing_finder(int(input()))

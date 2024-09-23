"""Missing Number No Set"""
def missing_finder(n):
    """Find the missing number"""
    all_number = []
    my_list = []
    for num in range(1, n+1):
        all_number.append(num)
    while True:
        number = int(input())
        if not number:
            break
        my_list.append(number)
    for number in sorted(all_number):
        if not number in my_list:
            print(number)
missing_finder(int(input()))

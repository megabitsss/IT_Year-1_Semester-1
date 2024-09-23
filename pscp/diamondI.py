"""Diamond I"""
def diamond_digger(depth, width):
    """Find the most worth hole to dig the diamonds"""
    row_list = []
    most = 0
    for _ in range(depth):
        diamond = input().split()
        diamond = tuple(map(int, diamond))
        row_list.append(diamond)
    for column in range(0, width):
        total = 0
        for row in row_list:
            total += row[column]
        if total > most:
            most = total
    print(most)
diamond_digger(int(input()), int(input()))

"""Almost Mean"""
def almost_mean(n):
    """find the number that is less and closest to mean"""
    my_list = []
    avg = 0
    most = 0
    most_student = None
    for _ in range(n):
        data = input()
        number = float(data[9:])
        my_list.append(data)
        avg += number
    avg /= n
    for item in my_list:
        number = float(item[9:])
        if most <= number <= avg:
            most = number
            most_student = item
    print(most_student)
almost_mean(int(input()))

"""Pick Them Again"""
def divisible_3_5(string):
    """filter the by the item that is divisible by 3 or 5 and reversed"""
    my_list = string.split()
    filtered_list = []
    for number_str in my_list:
        number_int = int(number_str)
        if not number_int % 3 or not number_int % 5:
            filtered_list.append(number_int) #added as integer
    if not filtered_list:
        print("Nope")
    else:
        for number in filtered_list[::-1]:
            print(number)
divisible_3_5(input())


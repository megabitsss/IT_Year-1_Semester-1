"""Kaprekar"""
def ascender(num):
    """ordering num asecendingly"""
    num_list = list(num)
    index_length = len(num_list) - 1 #no need to swap the last num with i+1 (out of index)
    for i in range(0, index_length):
        least_index = i
        for j in range(i+1, len(num_list)):
            if num_list[j] < num_list[least_index]:
                least_index = j
        if least_index != i:
            num_list[i], num_list[least_index] = num_list[least_index], num_list[i]
    return "".join(num_list)
def descender(num):
    """ordering num descendingly"""
    num_list = list(num)
    index_length = len(num_list) - 1
    for i in range(0, index_length):
        most_index = i
        for j in range(i+1, len(num_list)):
            if num_list[j] > num_list[most_index]:
                most_index = j
        if most_index != i:
            num_list[i], num_list[most_index] = num_list[most_index], num_list[i]
    return "".join(num_list) #concatenate each member in list with ("" as seperator)
def kaprekar_const_finder(num): #num (as string)
    """amount of time to get the karprekar's constant"""
    cnt = 0
    while int(num) != 6174:
        ascend_num = ascender(str(num).ljust(4, "0"))
        descend_num = descender(str(num).ljust(4, "0"))
        num = int(descend_num) - int(ascend_num)
        cnt += 1
    print(cnt)
kaprekar_const_finder(input())

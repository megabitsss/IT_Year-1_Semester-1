"""Kaprekar"""
def orderer(num, order_type):
    """ordering num in either ascending/descending"""
    num_list = list(num)
    index_length = len(num) - 1 #no need to swap the last num with i+1 (out of index)
    order_bool = False
    while not order_bool: #while it's not ordered
        order_bool = True
        for i in range(0, index_length):
            match order_type:
                case "ascend":
                    if num_list[i] > num_list[i+1]:
                        order_bool = False
                        num_list[i], num_list[i+1] = num_list[i+1], num_list[i]
                case "descend":
                    if num_list[i] < num_list[i+1]:
                        order_bool = False
                        num_list[i], num_list[i+1] = num_list[i+1], num_list[i]
    return "".join(num_list) #concatenate each member in list with ("" as seperator)
def kaprekar_const_finder(num): #num (as string)
    """amount of time to get the karprekar's constant"""
    cnt = 0
    while int(num) != 6174:
        ascend_num = orderer(str(num), "ascend")
        descend_num = orderer(str(num), "descend")
        num = int(descend_num) - int(ascend_num)
        cnt += 1
    print(cnt)
kaprekar_const_finder(input())

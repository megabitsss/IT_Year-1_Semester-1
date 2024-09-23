"""Cat Parade"""
def cat_counter():
    """Count each breed of cat"""
    unsorted_list = []
    sorted_list = []
    while True:
        cat = input()
        if cat == "IT'S A DOG":
            unsorted_list.pop()
            continue
        if cat == "END":
            break
        unsorted_list += cat.split(", ")
    for item in unsorted_list: #remove redundant item and sort the list
        if not item in sorted_list:
            sorted_list.append(item)
    sorted_list.sort()
    for item in sorted_list:
        print(item, unsorted_list.index(item)+1, unsorted_list.count(item))
cat_counter()

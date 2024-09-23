"""Pick Them"""
import json
def even_number_filter(string):
    """filter on even number in the list"""
    my_list = json.loads(string)
    even = False
    for item in my_list:
        if not item % 2: #if even
            print(item)
            even = True
    if not even:
        print("Nope")
even_number_filter(input())

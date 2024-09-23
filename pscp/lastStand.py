"""Last Stand"""
import json
def last_index(string):
    """return last character of each element in the list"""
    my_list = json.loads(string)
    for item in my_list:
        last_char = str(item)[-1]
        print(last_char)
last_index(input())

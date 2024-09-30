"""Gram_v1"""
def two_gram(txt):
    """find the most frequent 2-gram"""
    hz_dict = {}
    for index in range(0, len(txt)-1):
        string = txt[index:index+2]
        hz_dict[string] = hz_dict.get(string, 0) + 1
    key_list = list(hz_dict.keys())
    value_list = list(hz_dict.values())
    most_index = value_list.index(max(value_list))
    print(key_list[most_index])
    print(value_list[most_index])
two_gram(input())

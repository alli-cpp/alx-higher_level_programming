#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list.sort()
    prev = None
    res = 0
    for i in my_list:
        if i != prev:
            prev = i
            res += prev
    return 

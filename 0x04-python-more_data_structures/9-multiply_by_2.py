#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}
    for i in list(a_dictionary):
        new[i] = 2 * a_dictionary[i]
    return new

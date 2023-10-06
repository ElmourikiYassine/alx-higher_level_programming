#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx > len(my_list) or idx < 0:
        return my_list.copy()
    for i in range(len(my_list)):
        if i == idx:
            new_list = my_list.copy()
            new_list[i] = element
            return new_list

#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    return [(is_by2 % 2) == 0 for is_by2 in range(len(my_list))]

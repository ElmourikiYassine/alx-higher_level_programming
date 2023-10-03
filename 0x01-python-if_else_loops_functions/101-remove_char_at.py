#!/usr/bin/python3
def remove_char_at(str, n):
    str_cp = list(str)
    for i in range(len(str_cp)):
        if i == n:
            return ''.join(str_cp[:i] + str_cp[i+1:])
    return str

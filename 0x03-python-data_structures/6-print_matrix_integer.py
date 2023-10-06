#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for _list in matrix:
        for i in range(len(_list)):
            char = ' ' if i != (len(_list) - 1) else ''
            print("{}{}".format(_list[i], char), end='')
        print()

#!/usr/bin/python3
def uppercase(tmp_str):
    if tmp_str == "":
        print('\n', end='')
    else:
        tmp_list = list(tmp_str)
        for i in range(len(tmp_list)):
            if ord(tmp_list[i]) in range(97, 123):
                tmp_list[i] = chr(ord(tmp_list[i]) - 32)
            print("{}".format(tmp_list[i]), end='\n'
                  if i == len(tmp_list) - 1 else '')

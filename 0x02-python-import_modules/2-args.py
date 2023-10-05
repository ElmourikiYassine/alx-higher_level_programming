#!/usr/bin/python3

from sys import argv

if __name__ == '__main__':
    char = '.' if len(argv) == 1 else ':'
    print("{} arguments{}".format(len(argv) - 1, char))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
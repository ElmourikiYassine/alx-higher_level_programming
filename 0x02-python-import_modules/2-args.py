#!/usr/bin/python3

from sys import argv

if __name__ == '__main__':
    char = '.' if len(argv) == 1 else ':'
    print(f"{len(argv) - 1} arguments{char}")
    for i in range(1, len(argv)):
        print(f"{i}: {argv[i]}")

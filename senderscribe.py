#!/usr/bin/env python3

"""Reads from stdin and outputs to stdout the same sequence of bytes plus a
hash byte"""

import sys

def main(input, output):
    """Reads from stdin and outputs to stdout the same sequence of bytes plus a hash byte"""
    inputfile = input
    outputfile = output

    checker = 0
    byte = inputfile.read(1)
    if byte:
        print(to_unicode(byte))
    while byte:
        print(byte, end='', file=outputfile)
        checker += ord(byte)
        byte = inputfile.read(1)

    print(chr(ord('A')+(checker%25)), end='', file=outputfile)

def to_unicode(byte):
    if byte.isupper():
        return ord(byte) - ord('A')
    elif byte.isdigit():
        return ord(byte) - ord('0') + ord('Z') - ord('Z')
    else:
        return 0

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1], sys.argv[2])
    else:
        main(sys.stdin, sys.stdout)

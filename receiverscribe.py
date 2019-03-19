#!/usr/bin/env python3

"""Reads from stdin and outputs to stdout the same sequence of bytes and checks
the hash byte"""

import sys

def main():
    """Reads from stdin and outputs to stdout the same sequence of bytes and checks the hash byte"""
    inputfile = sys.stdin
    outputfile = sys.stdout

    checker = 0
    byte = inputfile.read(1)
    last_byte = ''
    while byte:
        checker += ord(byte)
        last_byte = byte
        byte = inputfile.read(1)

    checker -= ord(last_byte)
    checker = chr(ord('A')+(checker%25))

    if checker == last_byte:
        print('OK', file=outputfile)
    else:
        print('KO', file=outputfile)

if __name__ == "__main__":
    main()

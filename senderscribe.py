#!/usr/bin/env python3

"""Reads from stdin and outputs to stdout the same sequence of bytes plus a
hash byte"""
from binary_tree import BinaryTree
import sys

def main(inputf, outputf):
    """Reads from stdin and outputs to stdout the same sequence of bytes plus a hash byte"""
    inputfile = inputf
    outputfile = outputf
    string = '\n'
    bits_buits = 0

    bt = BinaryTree(None)
    bt = bt.put(7.5)


    byte = inputfile.read(1)
    if byte:
        print(byte, end='', file=outputfile)
        first_letter = to_unicode(byte)
        bits_buits = 2
        first_letter <<= 2

        last_byte = byte
        byte = inputfile.read(1)

    while byte:
        print(byte, end='', file=outputfile)
        shift += abs(to_unicode(byte) - to_unicode(last_byte))



        last_byte = byte
        byte = inputfile.read(1)

    print(": " + shift, end='\n', file=outputfile)

def to_unicode(byte):
    """ fadfas """
    if byte.isupper():
        return ord(byte) - ord('A')
    return ord(byte) - ord('0') + ord('Z') - ord('Z')

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1], sys.argv[2])
    else:
        main(sys.stdin, sys.stdout)

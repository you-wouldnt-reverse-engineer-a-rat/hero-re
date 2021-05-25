#!/usr/bin/env python3

import argparse
import os
import struct
import sys
from pathlib import Path

def find_offset(value_list):
    for offset in range(len(value_list)):
        if(value_list[offset] == 0x2E):
            return offset

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Format hex list (direct extract from mosi on logic analyzer startup) file to bin blob')
    parser.add_argument('-i', '--input', type=str,
                        help='Input file.')
    parser.add_argument('-b', '--binary', type=str,
                        help='binary to write.')
    parser.add_argument('-o', '--offset', type=str,
                        help='offset of srom, automatic if not specified')
    args = parser.parse_args()

    if not args.input or not os.path.exists(args.input):
        print(f'{args.input} doesn\'t exist', file=sys.stderr)
        exit(1)

    if not args.binary:
        print('binary file required.', file=sys.stderr)
        exit(1)

    try:
        binary = open(args.binary, 'wb')
    except PermissionError as e:
        print(f'can\'t open {args.binary}: {str(e)}', file=sys.stderr)
        exit(1)

    try:
        input_file = open(args.input, 'r')
    except PermissionError as e:
        print(f'can\'t open {args.input}: {str(e)}', file=sys.stderr)
        exit(1)

    value_list = []

    for line in input_file.readlines():
        value_list.append(int(line, 16))

    if not args.offset:
        offset = find_offset(value_list)
    else:
        offset = args.offset

    for value in value_list[offset+1:offset+(2*4096):2]:
        binary.write(bytes([value]))

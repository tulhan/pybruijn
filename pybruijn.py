#!/usr/bin/env python3

import math
import itertools

UPPERCASE = b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWERCASE = b'abcdefghijklmnopqrstuvwxyz'
NUMERALS = b'0123456789'


def generate(length, start=0):
    patterns = (UPPERCASE, LOWERCASE, NUMERALS)
    product = itertools.product(*patterns)
    if start:
        iters = int(math.ceil(start + length / len(patterns)))
    else:
        iters = int(math.ceil(length / len(patterns)))

    px = (bytearray(x) for _, x in zip(range(iters), product))
    long_pattern = b''.join(px)

    if length > len(long_pattern[:length]):
        raise IndexError("Pattern length > max:{}".format(len(long_pattern)))

    return long_pattern[start:start + length]


def offset(search_str):
    if len(search_str) < 3:
        raise SystemExit('Not enough search data to be unique')
    _ = generate(20280).find(search_str)

    return _


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Generate De Bruijn patterns')
    subparsers = parser.add_subparsers(dest='action')
    subparsers.required = True

    _generate = subparsers.add_parser('generate')
    _generate.add_argument('length')

    _offset = subparsers.add_parser('offset')
    _offset.add_argument('string')

    args = parser.parse_args()

    if args.action == 'generate':
        print(generate(int(args.length)))
    elif args.action == 'offset':
        string = args.string.encode('utf-8')
        _ = offset(string)
        if _ == -1:
            _ = offset(string[::-1])
            if _ == -1:
                raise SystemExit('Pattern not found')
            else:
                print(_)
        else:
            print(_)
    else:
        raise SystemExit('Unknown command')

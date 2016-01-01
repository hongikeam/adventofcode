#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, with_statement

def run(v):
    s = 0 
    for pos in range(0, len(v)):
        if v[pos] == '(':
            s += 1
        elif v[pos] == ')':
            s -= 1
        if s == -1:
            break
    print(pos + 1)

if __name__ == '__main__':
    import sys

    for line in sys.stdin:
        run(line)

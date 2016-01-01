#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, with_statement

def get_feet(v):
    arr = v.split('x')
    l = int(arr[0])
    w = int(arr[1])
    h = int(arr[2])
    _m = max(l, w, h)
    _two = [v for v in (l, w, h) if v < _m]
    for i in range(0, 3 - len(_two)):
        _two.append(_m)
    return l * w * h + (_two[0] + _two[1]) * 2

if __name__ == '__main__':
    import sys

    total = 0
    for line in sys.stdin:
        total += get_feet(line.strip())
    print(total)

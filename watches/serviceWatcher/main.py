#!/usr/bin/env python
# coding=utf-8
import sys

if __name__ == '__main__':
    path = '/data/code/dockerfile/consul/watches/serviceWatcher/test.txt'
    with open(path, 'wb') as f:
        f.write(str(sys.argv))

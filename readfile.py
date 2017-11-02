#!/usr/bin/python

with open('test.txt') as f:
    # read_data = f.read()
    for line in f:
        print(line)
f.closed

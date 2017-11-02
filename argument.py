#!/usr/bin/python
import sys
import os
filename  = sys.argv[1][0:-3]
print (filename)
splitname, spliextension = sys.argv[1].split('.')
print (splitname)
print (spliextension)
print (os.getcwd())

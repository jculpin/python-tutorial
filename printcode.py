#! /usr/bin/env python
import sys
import subprocess
import os
import shutil

filename = sys.argv[1]
#printfile = sys.argv[1][0:-3]
printfile, fileextension = sys.argv[1].split('.')

texfilename = printfile + ".tex"
pdffile = printfile + ".pdf"
logfile = printfile + ".log"
auxfile = printfile + ".aux"
minteddir = "_minted-" + printfile

if not os.path.isfile(filename):
    print("Error: %s file not found" % filename)
    sys.exit(1)
    
try:
    outfile = open(texfilename, 'w', 1)
except OSError, e:
	print ("Error: %s - %s." % (e.filename,e.strerror))  
	
if not os.path.isfile('template.tex'):
    print("Error: template.tex file not found")
    sys.exit(1)
    	
with open('template.tex') as infile:
    for line in infile:
        newline = line.replace("$1", filename)
        outfile.write(newline)
infile.closed
outfile.closed

try:
    subprocess.call(["pdflatex", "-shell-escape", texfilename])
except OSError, e:
	print ("Error: %s - %s." % (e.filename,e.strerror))
	
#try:	    
#    subprocess.call(["lpr", pdffile])
#except OSError, e:
#    print ("Error: %s - %s." % (e.filename,e.strerror))

try:
    os.remove(texfilename)
except OSError, e:
	print ("Error: %s - %s." % (e.filename,e.strerror))    
try:
    os.remove(logfile)
except OSError, e:
	print ("Error: %s - %s." % (e.filename,e.strerror))
try:
	os.remove(auxfile)
except OSError, e:
	print ("Error: %s - %s." % (e.filename,e.strerror))
try:
    shutil.rmtree(minteddir)
except OSError, e:
	print ("Error: %s - %s." % (e.filename,e.strerror))

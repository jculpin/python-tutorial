import pydoc
import sys

helpname = sys.argv[1]

strhelp = pydoc.render_doc(helpname, "Help on %s")

try:
    outfile = open("helpfileprint.txt", 'w', 1)
except OSError, e:
	print ("Error: %s - %s." % (e.filename,e.strerror))  
	
outfile.write(strhelp)
outfile.closed	

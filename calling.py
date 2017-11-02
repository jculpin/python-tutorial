#! /usr/bin/python

import subprocess

#subprocess.call(["ls", "-l"])
subprocess.call(["pdflatex", "-shell-escape", "demo.hs.tex"])

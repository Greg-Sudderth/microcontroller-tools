#!/usr/bin/python

import sys
import os

# mp3tocstruct.py: Read in a mp3 file (or other binary) and output as a .C and .H
# file for inclusion in a C program.  I used this to put a built-in-self-test MP3 into
# the RTI Media (rtimedia.com) Message On Hold player.  This lets the player be tested
# during manufacture without a SD card.
#
# Example output:
# unsigned char music[] = 
# { 
#     04, 91, 22, 55, 14, 19, 67
# };
#
# Author: Gregory R. Sudderth

argLen = len(sys.argv)
if argLen != 3:
    print "Usage: " + sys.argv[0] + " structname infile.mp3"
    sys.exit(1)

hasWrittenHeaderYet = False
structName = sys.argv[1]
outFileNameC = structName + ".c"
outFileNameH = structName + ".h"
inMP3FileName = sys.argv[2]

totalMP3FileLength = os.path.getsize(inMP3FileName)

with open(outFileNameC, "w") as outfile:
    with open(inMP3FileName) as infile:
        while True:
            chunk = infile.read(16)
            if chunk:
                if not hasWrittenHeaderYet:
                    outfile.write("unsigned char " + structName + "[] = ")
                    outfile.write("{")
                    hasWrittenHeaderYet = True
                outfile.write("    "),
                for b in chunk:
                    outfile.write((str(ord(b)) + ", ")),
                outfile.write("\n")
            else:
                break
    outfile.write("};")
    with open(outFileNameH, "w") as outFileH:
        outFileH.write("#define " + structName.upper() + "_SIZE " +
                       str(totalMP3FileLength) + "\n")

sys.exit(0)

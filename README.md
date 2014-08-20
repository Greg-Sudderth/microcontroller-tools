microcontroller-tools
=====================

Micro controller tools to help with programming on PIC, AVR, etc.

** mp3tocstruct.py: 

Read in a mp3 file (or other binary) and output as a .C and .H file for inclusion in a C program.  
I used this to put a built-in-self-test MP3 into the RTI Media (rtimedia.com) Message On Hold player.  
This lets the player be tested during manufacture without a SD card.

Usage: ./mp3tocstruct.py music mysamplemusic.mp3

This creates music.c, and music.h, and creates a unsigned char music[] with the appropriate verbatim data.  Uses Python 2.7.


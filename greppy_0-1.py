#!/usr/bin/python2

###############      GrepPy 0.1 - Python 2.x regular expression parser
#
#  Usage python greppy_0-1.py PATTERN STRING
# 
#  The stages of development will be as follows:
#  * Stage 1 - Simple python script evaluating a given string with a given regular expression string and outputting to std out
#    Stage 2 - Add file input support and allow specification of delimiter and output format. Clean up commandline options
#    Stage 3 - Add common greps to options, and have some config files with parser. IP's.
#    Stage 4 - Tighten up encapsulation
#    Stage 5 - Allow expression lists
#    Stage 6 - Port to C, test and package for deployment
#
###############

## Research - how to represent

import re, sys

# Globals
pattern=''
inString=''

# option parser
if len(sys.argv) != 3:
    print('check your arguments')
    sys.exit(0)
else:
    pattern=str(sys.argv[1])
    inString=str(sys.argv[2])

def main():
    matchList=[]
    matchList=re.findall(pattern,inString)
    for i in range(len(matchList)):
        print i + ':  '+matchList[i]

# run main loop and exit cleanly
if __name__ == '__main__':
     main()
     print 'exiting'
     sys.exit(0)


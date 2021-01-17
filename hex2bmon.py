#!/usr/bin/python3
#
# This will take an Intel Hex file and convert it to the format
# used by Lee Hart's 6502 Badge monitor program.
#
# By Jim McClanahan, W4JBM (Jan 2021)
#

import sys

# Check for command line argument and print an intro if
# none was provided...
if len(sys.argv) != 3:
    print("Convert Intel Hex file to the 6502 Badge's monitor format.")
    print("USAGE: hex2bmon.py filename.hex filename.mon")
    sys.exit(1)

with open(sys.argv[1]) as f1:
    with open(sys.argv[2], "w") as f2:
        for line in f1:
            if ((len(line) == 0) or (line[0] != ':')):
                continue;
            else:
                num_dig = int(line[1:3],16)
                if num_dig == 0:
                    continue;
                temp_line = line[3:7] + ':'
                for x in range(num_dig):
                    if x == 16:
                        xa = int(line[3:7],16) + 16
                        temp_line += '\n' + '{0:04X}'.format(xa) + ':'
                    x1 = x*2 + 9
                    x2 = x*2 + 11
                    temp_line += line[x1:x2] + ' '
#               print("%s" % temp_line)
                temp_line += '\n'
                f2.write(temp_line)


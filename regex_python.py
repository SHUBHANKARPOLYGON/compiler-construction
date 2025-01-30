# Consider the following Regular Expression (0+1)*+0*1* and write a Python program for the regular expression.
#(0+1)*+0*1*
#sigma,0,1,01,10

import re

# Regular Expression pattern
pattern = r"(0|1)*0*1*"

# Sample input strings to check against the regex
strings = ["0", "1", "01", "10", "001", "010", "101", "110", "000", "111", "0000", "1111", "0001", "0011", "0101", "0110", "1010", "1100", "1001", "1110", "1011", "1101", "0111", "0100", "0010"]

# Check each strings if it matches the regex pattern

for s in strings:
    if re.fullmatch(pattern, s):
        print(f"'{s}' is a match")
    else:
        print(f"'{s}' is not a match")
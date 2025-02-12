# Consider the following Regular Expression (0+1)*+0*1* and write a Python program for the regular expression.
#(0+1)*+0*1*
#sigma,0,1,01,10

import re

# Regular Expression pattern
pattern = r"(0|1)*0*1*"

# Sample input strings to check against the regex
strings = ["0", "1", "00", "11", "125", "111", "211"]

# Check each strings if it matches the regex pattern

for s in strings:
    if re.fullmatch(pattern, s):
        print(f"'{s}' is a match")
    else: 
        print(f"'{s}' is not a match")
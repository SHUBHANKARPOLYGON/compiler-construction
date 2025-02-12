import re

# Regular Expression pattern for question 3
pattern = r'^((a|b)(c|d)|ab*c*d)$'

# Sample input strings to check against the regex
strings = ["acd", "bd", "abc", "abbbcd", "xyz", "a", "bcd"]

# Check each string if it matches the regex pattern
for s in strings:
    if re.fullmatch(pattern, s):
        print(f"'{s}' is a match")
    else:
        print(f"'{s}' is not a match")
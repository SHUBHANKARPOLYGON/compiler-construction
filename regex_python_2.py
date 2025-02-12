# Consider the following regular expressions:
# a)	(ab*c + (def)+ + ad+e)+

import re

def test_regex(pattern, test_strings):
    compiled_pattern = re.compile(pattern)
    for string in test_strings:
        match = compiled_pattern.fullmatch(string)
        print(f"'{string}' -> {'Matches' if match else 'Does not match'}")

# Regular expressions
# regex_a = r'(0|1)*|0*1*'
regex_a = r'(ab*c|(def)+|ad+e)+'

# Test cases
# strings_a = ["", "0", "1", "01", "10", "111", "000111", "11000"]
strings_a = ["abc", "defdef", "ade", "abbc", "aade", "abcdef", "aaddde"]

# print("Testing regex a:")
# test_regex(regex_a, strings_a)
print("Testing regex :")
test_regex(regex_a, strings_a)

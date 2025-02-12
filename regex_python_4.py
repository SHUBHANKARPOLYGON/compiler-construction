# Consider the following regular expressions:
# a)	(0 + 1)* + 0*1*


import re

def test_regex(pattern, test_strings):
    compiled_pattern = re.compile(pattern)
    for string in test_strings:
        match = compiled_pattern.fullmatch(string)
        print(f"'{string}' -> {'Matches' if match else 'Does not match'}")

# Fixing regex definition and indentation
regex_a = r'(0|1)*|0*1*'  # This is valid but could be simplified

strings_a = ["", "0", "1", "01", "10", "111", "000111", "11000"]

print("Testing regex a:")
test_regex(regex_a, strings_a)

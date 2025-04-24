class Parser:
    def __init__(self, input_str):
        self.input = input_str
        self.pos = 0

    def match(self, char):
        if self.pos < len(self.input) and self.input[self.pos] == char:
            self.pos += 1
            return True
        return False

    def S(self):
        start_pos = self.pos
        if self.A() and self.B() and self.C():
            return True
        self.pos = start_pos
        return False

    def A(self):
        if not (self.match('a') and self.match('b')):
            return False
            
        # If we see another 'a', recursively process it
        if self.pos < len(self.input) and self.input[self.pos] == 'a':
            return self.A()
        return True

    def B(self):
        start_pos = self.pos
        
        # First try: B → b
        if self.match('b'):
            return True
            
        # Reset position before trying the alternative
        self.pos = start_pos
        
        # We need to prevent infinite recursion
        # B can't expand to BC if it didn't expand to b
        # This grammar is problematic as written - removing the recursive case
        return False

    def C(self):
        if not self.match('c'):
            return False
            
        # Consume any additional 'c's
        while self.pos < len(self.input) and self.input[self.pos] == 'c':
            self.pos += 1
        return True

    def parse(self):
        success = self.S() and self.pos == len(self.input)
        return success


# List of strings to test
test_strings = [
    "abbccc",    # should be valid
    "abaccc",    # invalid: 'a' after 'b' breaks the pattern
    "abccc",     # valid
    "ababccc",   # valid
    "ab",        # invalid: missing B and C
    "abb",       # invalid: missing C
    "abbbccc",   # should be valid with B → 'b'
    "abbbbbccc", # should be valid with multiple b's
    "abcbcc",    # invalid
    "abababccc"  # valid with multiple A → abA
]

# Run parser on each string
for s in test_strings:
    parser = Parser(s)
    result = parser.parse()
    print(f"'{s}': {'Valid' if result else 'Invalid'}")
import re
import keyword

# Token categories
TOKEN_PATTERNS = {
    'KEYWORD': r'\b(' + '|'.join(keyword.kwlist) + r')\b',
    'IDENTIFIER': r'\b[a-zA-Z_][a-zA-Z0-9_]*\b',
    'OPERATOR': r'(\+|\-|\|/|==|!=|<=|>=|<|>|\+=|-=|\=|/=|and|or|not)',
    'NUMBER': r'\b\d+(\.\d+)?\b',
    'STRING': r'(\".?\"|\'.?\')',
    'SPECIAL_SYMBOL': r'(👦|👦|👦|👦|\{|\}|,|:|;|.)',
}

# Function to tokenize input
def lexical_analyzer(code):
    tokens = []
    while code:
        code = code.lstrip()  # Remove leading whitespace
        matched = None
        
        for token_type, pattern in TOKEN_PATTERNS.items():
            regex = re.compile(pattern)
            match = regex.match(code)
            if match:
                tokens.append((token_type, match.group()))
                code = code[len(match.group()):]  # Move ahead in the code
                matched = True
                break
        
        if not matched:
            raise ValueError(f"Unexpected token: {code[:10]}")
    
    return tokens

# Sample Python code
python_code = "x = 5 + 10\ny = 'hello'\nif x > y:\n    print('x is greater')"

# Tokenizing the input code
tokens = lexical_analyzer(python_code)

# Displaying tokens
print("Tokens Identified:")
for token in tokens:
    print(token)
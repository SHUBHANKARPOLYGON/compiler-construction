import re

def convert_re_to_grammar(regex):
    """Convert a given regular expression into regular grammar rules."""
    grammar = {}
    start_symbol = 'S'  # Default start symbol
    next_non_terminal = 'A'  # Next available non-terminal
    counter = 0  # To generate unique non-terminals

    # Function to add production rules in a compact form
    def add_rule(non_terminal, production):
        if non_terminal in grammar:
            grammar[non_terminal].add(production)
        else:
            grammar[non_terminal] = {production}

    # Processing the regex
    regex = regex.replace(" ", "")  # Remove spaces if any
    tokens = re.split(r'(\||\*|👦|👦)', regex)  # Tokenize based on regex operators
    stack = [start_symbol]  # Stack to hold non-terminals

    for token in tokens:
        if token == '' or token == '(' or token == ')':
            continue
        elif token == '|':  # OR condition
            stack.append(stack[-1])  # Duplicate last non-terminal for parallel production
        elif token == '*':  # Kleene star (repeatable)
            add_rule(stack[-1], stack[-1])  # Allow repetition
            add_rule(stack[-1], 'ε')  # Allow empty transition
        else:
            new_symbol = next_non_terminal + str(counter)
            counter += 1
            add_rule(stack[-1], token + new_symbol)
            stack.append(new_symbol)

    # Formatting grammar rules
    formatted_rules = []
    for non_terminal, productions in grammar.items():
        formatted_rules.append(f"{non_terminal} → {' | '.join(sorted(productions))}")

    return formatted_rules

def write_grammar_to_file(grammar_rules, filename="Regular_Grammar.txt"):
    """Write grammar rules to a file, one per line."""
    with open(filename, "w") as file:
        for rule in grammar_rules:
            file.write(rule + "\n")
    print(f"Grammar saved to {filename}")

# Get user input for Regular Expression
regex_input = input("Enter a regular expression: ")

# Convert RE to Regular Grammar
grammar_rules = convert_re_to_grammar(regex_input)

# Print and save the grammar
print("\nGenerated Regular Grammar:\n")
for rule in grammar_rules:
    print(rule)

write_grammar_to_file(grammar_rules)
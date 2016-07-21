"""Write an algorithm that reads a string from left to right and returns T if
the parentheses are balanced."""

# (2) --> T
# (2 + 3)) --> F
# (2+ 3)) - ()
# (2 + 3) - ((
# ( --> F
# ((((2 + 3) * 5)) --> F
# ()(

def balanced_parentheses(str):

    parens = []

    for char in str:
        if char == '(':
            parens.append(char)
        elif char == ')':
            if not parens:
                return False
            parens.pop()

    if parens:
        return False
    return True

print balanced_parentheses('(2)')
print balanced_parentheses('(2 + 3))')
print balanced_parentheses('(')
print balanced_parentheses("((((2 + 3) * 5))")








"Given a string, return true if it contains balanced parenthesis  ()."

def balanced_parens(string):

    parens = []

    for char in string:
        if char == '(':
            parens.append(char)
        elif char == ')':
            if not parens:
                return False
            parens.pop()

    if parens:
        return False

    return True



print balanced_parens('(())')
print balanced_parens('(((()')
print balanced_parens("")
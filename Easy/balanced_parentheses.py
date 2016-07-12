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
    # add parens to list
    # pop when there is a set of matching parens()

    parens = []

    for char in str:
        if char == '(':
            parens.append(char)
        elif char == ')':
            if not parens or parens[-1] == ')':
                return False
            elif parens[-1] == '(':
                parens.pop()

    if parens:
        return False
    return True

balanced_parentheses('(2)')
balanced_parentheses('(2 + 3))')
balanced_parentheses('(')
balanced_parentheses("((((2 + 3) * 5))")








"""Count items in a list recursively.

For example:

        >>> count_recursively([])
        0

        >>> count_recursively([1, 2, 3])
        3

"""
# Strategy: length of the list equals length of the first item of the list +
# the length of the rest of the list. 

def count_recursively(lst):
    """Return number of items in a list, using recursion."""

    # base case
    if len(lst) == 0:
        return 0

    # recursive function call
    return 1 + count_recursively(lst[1:])

def count_to_three(n):

    n = 1

    while n<=3:
        print n
        n += 1


def count_to_three_recursively(n=1):

    if n > 3:
        return

    print n
    count_to_three_recursively(n+1)


    

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GO YOU!\n"

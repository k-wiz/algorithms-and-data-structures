"""Count items in a list recursively.

For example:

        >>> count_recursively([])
        0

        >>> count_recursively([1, 2, 3])
        3

"""
# 1. So, you want me to write a function that takes in a list and returns the length of the list using recursion?
# 2. What if I get an empty list? 
# 3. Test cases: 
# 4. Strategy: The length of the list equals the length of the first item + the length of the rest of the list. 
# 5. My base case is an empty list, which returns 0. Then I'll call the function recursively on the rest of the list. 


def count_recursively(lst):
    """Return number of items in a list, using recursion."""


    if lst == []:
        return 0

    return 1 + count_recursively(lst[1:])


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GO YOU!\n"


# 1 + recurse([2,3])
# 1 + 1 + recurse([3])
# 1 + 1 + 1 + recurse([])
# 1 + 1 + 1 + 0



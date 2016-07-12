"""Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.

For example:

    >>> recursive_index(5, [1, 3, 5, 2, 4])
    2

    >>> recursive_index("hey", ["hey", "there", "you"])
    0

    >>> recursive_index("you", ["hey", "there", "you"])
    2

    >>> recursive_index("zork", ["foo", "bar", "baz"]) is None
    True

"""


def recursive_index(needle, haystack):
    """Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.
    """

    if needle not in haystack:
        return None

    if haystack == []:
        return 0

    # if item at index == haystack, return index 
    if haystack[0] == needle:
        return 0

    # if item at index != needle, add 1 to index and check rest of list. 
    return 1 + recursive_index(needle, haystack[1:])

    # def _recursive_index(needle, haystack, index):

    #     # Check if not found (we've gone too far)
    #     if index == len(haystack):
    #         return None

    #     # Have we found it?
    #     if haystack[index] == needle:
    #         return index

    #     return _recursive_index(needle, haystack, index + 1)

    # return _recursive_index(needle, haystack, 0)



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GO GO GO!\n"

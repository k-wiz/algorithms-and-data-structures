"""Given already-sorted lists, `a` and `b`, return sorted list of both.

You may not use sorted() or .sort().

Check edge cases of empty lists:

    >>> sort_ab([], [])
    []

    >>> sort_ab([1, 2,3], [])
    [1, 2, 3]

    >>> sort_ab([], [1, 2, 3])
    [1, 2, 3]

Check:

    >>> sort_ab([1, 3, 5, 7], [2, 6, 8, 10])
    [1, 2, 3, 5, 6, 7, 8, 10]
"""


def sort_ab(a, b):
    """Given already-sorted lists, `a` and `b`, return sorted list of both.

    You may not use sorted() or .sort().
    """
    #[1,2,3], [4,5] --> [1,2,3,4,5]

    sorted_ab = []
    #Strategy: 
    # If either list is empty, append the rest of other list. 
    while len(a) > 0 or len(b) > 0:
        if a == []:
            sorted_ab.append(b.pop(0))
        elif b == []:
            sorted_ab.append(a.pop(0))
        elif a[0] < b[0]:
            sorted_ab.append(a.pop(0))
        else:
            sorted_ab.append(b.pop(0))

    return sorted_ab



    # compare first number of each, append bigger to a new list. 


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU'RE A MERGE CHAMPION!!\n"

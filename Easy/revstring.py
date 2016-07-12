"""Reverse a string.

For example::

    >>> rev_string("")
    ''

    >>> rev_string("a")
    'a'

    >>> rev_string("porcupine")
    'enipucrop'

"""


def rev_string(astring):
    """Return reverse of string.

    You may NOT use the reversed() function!
    """
    # METHOD 1: 
    # rev_string = ""
    # for char in astring:
    #     rev_string = char + rev_string

    # return rev_string

    # METHOD 2: 
    # char_list = list(astring)

    # for i in range(len(char_list) / 2):
    #     char_list[i], char_list[-i - 1] = char_list[-i - 1], char_list[i]

    # return "".join(char_list)

    # METHOD 3:
    return astring[::-1]




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. !KROW DOOG\n"

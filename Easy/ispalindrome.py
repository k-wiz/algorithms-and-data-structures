"""Is this word a palindrome?

    >>> is_palindrome("a")
    True

    >>> is_palindrome("noon")
    True

    >>> is_palindrome("racecar")
    True

    >>> is_palindrome("porcupine")
    False

Treat spaces and uppercase letters normally:

    >>> is_palindrome("Racecar")
    False
"""
#Strategy: 



def is_palindrome(word):
    """Return True/False if this word is a palindrome."""

    # SOLUTION 1: 
    # word_list = []

    # for char in word:
    #     word_list.append(char)

    # reversed_word_list = word_list[::-1]

    # if word_list == reversed_word_list:
    #     return True
    # return False

    # SOLUTION 2: 
    # reversed_word = ""

    # for char in word:
    #     reversed_word = char + reversed_word

    # if word == reversed_word:
    #     return True
    # return False

    # SOLUTION 3: 
    #Compare first letter to last letter. 0 to -1, 1 to -2, 

    for i in range (len(word) / 2):
        if word[i] != word[-1 - i]:
            return False
    return True








if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YAY!"

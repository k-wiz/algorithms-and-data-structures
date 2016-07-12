"""Reverse list in place.

You cannot do this with reversed(), .reverse(), or list slice
assignment!

    >>> lst = []
    >>> rev_list_in_place(lst)
    >>> lst
    []

    >>> lst = ['a']
    >>> rev_list_in_place(lst)
    >>> lst
    ['a']

    >>> lst = [1, 2, 3]
    >>> rev_list_in_place(lst)
    >>> lst
    [3, 2, 1]

    >>> lst = [1, 2, 3, 4]
    >>> rev_list_in_place(lst)
    >>> lst
    [4, 3, 2, 1]
"""



#CANT REVERSE STRING IN PLACE, ITS IMMUTABLE, duh! 
# def rev_string(str):

#     for i in range(len(str)/2):
#         str[i], str[-i-1] = str[-i-1], str[i]   

#     return str


def rev_string(str):
    return str[::-1]


def reverse_words_in_string(str):

    #split words --> list of words
    #call rev_string on each word in list
    #.join

    word_list = str.split(" ")
    reverse_word_list = []
    for word in word_list:
        reverse_word_list.append(rev_string(word))

    print " ".join(reverse_word_list)
    return " ".join(reverse_word_list)

reverse_words_in_string("kelli is cool")




def rev_list_in_place(lst):
    """Reverse list in place.

    You cannot do this with reversed(), .reverse(), or list slice
    assignment!
    """
    for i in range(len(lst)/2):
        lst[i], lst[-1 - i] = lst[-1 - i], lst[i]





if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU'RE THE BEST!\n"

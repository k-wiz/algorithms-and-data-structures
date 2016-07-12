"""Split astring by splitter and return list of splits.

This should work like that built-in Python .split() method [*].
YOU MAY NOT USE the .split() method in your solution!
YOU MAY NOT USE regular expressions in your solution!

For example:

    >>> split("i love balloonicorn", " ")
    ['i', 'love', 'balloonicorn']

    >>> split("that is which is that which is that", " that ")
    ['that is which is', 'which is that']

    >>> split("that is which is that which is that", "that")
    ['', ' is which is ', ' which is ', '']

    >>> split("hello world", "nope")
    ['hello world']

* Note: the actual Python split method has special behavior
  when it is not passed anything for the splitter -- you do
  not need to implemented that.

"""


def split(astring, splitter):
    """Split astring by splitter and return list of splits."""

    word_list = []
    index = 0 

    while index <= len(astring):
        curr_index = index
        index = astring.find(splitter, index)

        if index != -1:
            word_list.append(astring[curr_index:index])
            index = index + len(splitter)

        else:
            word_list.append(astring[curr_index:])
            break

    return word_list

    #"I love kelli', 'love'






    # NOTE: Below solution only works for splitters that are single characters. 
    # word = ""
    # split_string = []

    # for char in astring:
    #     if char != splitter:
    #         word = word + char
    #         print "word", word
    #     elif char == splitter:
    #         split_string.append(word)
    #         print split_string
    #         word = ""
    # if word:
    #     split_string.append(word)
    # return split_string


    # word = ""
    # split_string = []

    # for char in astring:
    #     word = word + char
    #     print "word", word
    #     if word == splitter:


    #     split_string.append(word)
    #     print split_string
    #     word = ""
    # if word:
    #     split_string.append(word)
    # return split_string

# ['kelli rocks']



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. FINE SPLITTING!\n"

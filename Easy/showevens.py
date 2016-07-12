"""Given list of ints, return list of *indices* of even numbers in list.

For example::

    >>> show_evens([])
    []

    >>> show_evens([2])
    [0]

    >>> show_evens([1, 2, 3, 4])
    [1, 3]

"""


def show_evens(nums):
    """Given list of ints, return list of *indices* of even numbers in list."""

    # METHOD 1:
    # index = 0
    # index_list = []
    # for num in nums:
    #     if num % 2 == 0:
    #         index_list.append(index)
    #     index += 1

    # return index_list

    # METHOD 2:
    indices = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            indices.append(i)

    return indices



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. EVENLY HANDLED!\n"

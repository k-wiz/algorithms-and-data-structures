"""Return n unique random numbers from 1-10 (inclusive).

Given the numbers 1-10, return `n` random numbers, making sure
to never return the same number twice. You can trust that this
function will never be called with n < 0 or n > 10.

It's tricky to test random functions! However, we can make sure
asking for zero numbers gives us an empty list::

    >>> lucky_numbers(0)
    []

And if we ask for all numbers, we shouldn't get any repeats::

    >>> sorted(lucky_numbers(10))
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""

import random

def lucky_numbers(n):
    """Return n unique random numbers from 1-10 (inclusive)."""

    nums =  range(1,11)
    lucky_num_list = []

    for i in range(n):
        num = random.choice(nums)
        lucky_num_list.append(num)
        nums.remove(num)

    return lucky_num_list



def lucky_numbers2(n):

    return random.sample(range(1,11), n)

print lucky_numbers2(10)






if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT!\n"

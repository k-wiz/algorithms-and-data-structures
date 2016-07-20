"""Given a list of numbers 1...max_num, find which one is missing in a list."""


def missing_number(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list
    """

    """ Time complexity is O(n); space complexity is O(n)."""

    nums = set(nums)

    for i in range(1, (max_num + 1)):
        if i not in nums:
            return i


def missing_num(nums, max_num):
    """ Time complexity is O(nlogn), but space complexity is O(1)."""
    
    nums.sort()

    for i in range(1, len(nums)-1):
        if nums[i] + 1 != nums[i+1]:
            return (nums[i] + 1)


print missing_num([5,2,4,1], 5)



def missing_item(nums, max_num):
    """Time complexity is O(n), space complexity is O(1)."""

    nums_total = 0
    expected_total = sum(range(1, max_num+1))

    for num in nums:
        nums_total += num

    return expected_total - nums_total  

print missing_item([5,2,4,1], 5)






if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASS. NICELY DONE!\n"


def twoSum(arr, S):
    """Returns all pairs in the list that sum up to S. O(n^2)."""

    sums = []

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == S:
                sums.append([arr[i], arr[j]])

    return sums



def twoSum2(arr, S):
    """Optimized solution. O(n)."""
    
    sums = []
    sums_set = set()

    for i in range(len(arr)):
        sum_minus_element = S - arr[i]
        if sum_minus_element in sums_set:
            sums.append([arr[i], sum_minus_element])
        sums_set.add(arr[i])

    return sums

print twoSum2([0, 1, 1, 1, 2], 2)
print twoSum([0, 1, 1, 1, 2], 2)
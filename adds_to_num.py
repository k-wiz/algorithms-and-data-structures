"""Return all pairs of numbers in an array that add to n."""

# [1, 5, 3, 3, 2],  --> [(1,5), (3,3)]

def adds_to_num(lst, num):

    pairs = []

    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == num:
                pairs.append((lst[i], lst[j]))

    return pairs




print adds_to_num([1, 5, 3, 3, 2], 6)
print adds_to_num([], 5)


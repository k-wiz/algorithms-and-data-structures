
def add_one(lst):
    "Adds 1 to each item of the lst in place."
    for i in range(len(lst)):
        lst[i] = lst[i] + 1
    return lst


add_one([1,2,3])
add_one([])


def sort_array_with_zeros_ones(lst):

    zeros = []
    ones = []

    for num in lst:
        if num:
            ones.append(num)
        else:
            zeros.append(num)

    print zeros + ones


def sort_array_with_zeros_and_ones(lst):

    count_dict = {}
    for num in lst:
        count_dict[num] = count_dict.get(num,0) + 1

    return [0]*count_dict[0] + [1]*count_dict[1]

print sort_array_with_zeros_and_ones([0,1,0,1,0,0])
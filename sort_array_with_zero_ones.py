

def sort_array_with_zeros_ones(lst):

    zeros = []
    ones = []

    for num in lst:
        if num:
            ones.append(num)
        else:
            zeros.append(num)

    print zeros + ones


sort_array_with_zeros_ones([0,1,0,1,0,0])
#Given list of ints, return True if any two nums in list sum to 0.

#input --> a list of ints 
#output --> True / False 

#empty list? --> return False 
#non-ints? --> list will only include ints 

#[0, 1, 2, 3] --> False
#[-1, 1, 1] --> True
#[] --> False 

#This solution returns a false positive in lists that include 0! 

def sum_to_zero(lst):

    set_nums = set(lst)

    for num in lst:
        if -num in set_nums:
            return True

    return False





def sum_to_zero(lst):

    set_nums = set(lst)

    for x in lst:
        for y in lst[1:]:
            if x + y == 0:
                return True
    else:
        return False


sum_to_zero([0,1,2,3])

sum_to_zero([-1,1,1])

sum_to_zero([])

sum_to_zero([0,-1])













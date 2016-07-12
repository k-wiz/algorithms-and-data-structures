# Remove all duplicates from an unsorted array.
# [1,1,4,2,8] --> [1,4,2,8]
# [3,3,3] --> [3]
# [1,2,3] --> [1,2,3]
# [] --> []

# Can I create a new list, or do you want me to do it in place? (space)
# Do you want it returned in the same order?

# Returns a new list, NOT in original order. O(n) time. 
def remove_duplicates(lst):
    print  list(set(lst))
    return list(set(lst))

remove_duplicates([1,2,4,2,3])
remove_duplicates([3,3,3])
remove_duplicates([1,2,3])
remove_duplicates([])


# Creates a new list, returns it in the same order. O(n^2) time.
def remove_duplicates_2(lst):

    de_duped_list = []

    for item in lst:
        if item not in de_duped_list:
            de_duped_list.append(item)

    print de_duped_list
    return de_duped_list

remove_duplicates_2([1,2,4,2,3])
remove_duplicates_2([3,3,3])
remove_duplicates_2([1,2,3])
remove_duplicates_2([])




# Creates a new list, returns it in same order, but optimized to O(n) time.
def remove_duplicates_3(lst):

    seen = set([])
    unique = []
    
    for item in lst:
        if item not in seen:
            seen.add(item)
            unique.append(item)
            

    print unique
    return unique


remove_duplicates_3([1,2,4,2,3])
remove_duplicates_3([3,3,3])
remove_duplicates_3([1,2,3])
remove_duplicates_3([])



# Removes duplicates in place. Returns same list. 
# NOTE: I want to remove the duplicates in place, but I'm not sure how to 
# implement. Throws index error because when you delete an item, 
# the length of the list decreases by 1. How can I work around this?
def remove_duplicates_4(lst):

    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                del lst[j]
    print lst
    return lst

remove_duplicates_4([1,2,4,2,3])
remove_duplicates_4([3,3,3])
remove_duplicates_4([1,2,3])
remove_duplicates_4([])


# def unique(l):
#     s = set() 
#     n = 0
#     for x in l:
#         if x not in s: 
#             s.add(x) 
#             # l[n] = x
#             n += 1
#         del l[n]

#     print "unique", l
#     return l



# unique([1,2,4,2,3])
# unique([3,3,3])
# unique([1,2,3])
# unique([])

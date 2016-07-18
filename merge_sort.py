#1. recursively break list down into halves until len(lst) == 1.
#2. Merge two lists back together.


def merge_ordered_lists(lst1, lst2):

    merged_list = []
    while lst1 or lst2:
        if len(lst1) == 0:
            merged_list.extend(lst2)
            return merged_list

        if len(lst2) == 0:
            merged_list.extend(lst1)
            return merged_list

        if lst1[0] < lst2[0]:
            merged_list.append(lst1.pop(0))
        else:
            merged_list.append(lst2.pop(0))

    return merged_list


def merge_sort(lst):

    if len(lst) == 0 or len(lst) == 1:
        print lst
        return lst

    mid = len(lst)/2
    lst1 = lst[:mid]
    lst2 = lst[mid:]

    merge_sort(lst1)
    merge_sort(lst2)

    merged_list = []
    while lst1 or lst2:
        if len(lst1) == 0:
            merged_list.extend(lst2)
            return merged_list

        if len(lst2) == 0:
            merged_list.extend(lst1)
            return merged_list

        if lst1[0] < lst2[0]:
            merged_list.append(lst1.pop(0))
        else:
            merged_list.append(lst2.pop(0))

    return merged_list


print merge_sort([1,3,2,5])


"""Find the first item that occurs an even number of times in an array. 
Remember to handle multiple even-occurrence items and return the first one. 
Return null if there are no even-occurrence items."""

def even_occurrence(lst):

    item_count = {}

    for item in lst: 
        item_count[item] = item_count.get(item, 0) + 1

    for item in lst:
        if item_count[item] % 2 == 0:
            return item
        else:
            return None

print even_occurrence([1,2,3,4,5,1])
print even_occurrence(['h', 'h', 3, 3, 4, 4])
print even_occurrence([1])
print even_occurrence([])


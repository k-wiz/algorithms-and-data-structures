# Sort an array using bubblesort. Can you micro-optimize the runtime? 

# [1,7,3,7,2,0] --> [0,1,2,3,7,7]
# [0] --> [0]
# [] --> []


def bubblesort(lst):

    for i in range(len(lst)):
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

    return lst

print bubblesort([1,7,3,7,2,0])
print bubblesort([0])
print bubblesort([])


def bubblesort_optimized(lst):

    made_swap = False

    for i in range(len(lst)):
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                made_swap = True
        
        if made_swap == False:
            return lst

    return lst

print bubblesort_optimized([1,7,3,7,2,0])
print bubblesort_optimized([0])
print bubblesort_optimized([])
print bubblesort_optimized([0,1,2,3,4,5])


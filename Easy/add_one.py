# def add_one(lst):
#     for num in lst:
#         num = num + 1
#         print num
#         print lst
#     return lst 




def add_one(lst):
    for i in range(len(lst)):
        lst[i] = lst[i] + 1
    return lst

add_one([1,2,3])
add_one([])
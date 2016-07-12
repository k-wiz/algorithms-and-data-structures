def char_count(str):

    str_dict = {}

    for char in str:
        count = str_dict.get(char, 0)
        str_dict[char] = count + 1

    return str_dict



def one_edit_away(str1, str2):
    """Returns T if str1 and str2 are one edit (insert, replace, or delete) 
    or less away from each other."""

    if abs(len(str1) - len(str2)) > 1:
        return False

    str1_dict = char_count(str1)
    str2_dict = char_count(str2)

    differences = 0

    if len(str1) > len(str2): 
        for char in str1_dict.keys():
            if str1_dict[char] != str2_dict.get(char, 0):
                differences += 1
                
    else:
        for char in str2_dict.keys():
            if str2_dict[char] != str1_dict.get(char, 0):
                differences += 1

    if differences > 1:
        return False

    return True


print one_edit_away('pale', 'bale') #T
print one_edit_away('pales', 'pale') #T
print one_edit_away('pale', 'bae') #F





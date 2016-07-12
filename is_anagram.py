def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

def is_anagram2(str1, str2):
    dict1 = char_count(str1)
    dict2 = char_count(str2)

    return dict1 == dict2



def char_count(str):
    dict = {}
    for char in str:
        dict[char] = dict.get(char, 0) + 1
    return dict

print is_anagram("kelli", "illek")
print is_anagram("sdfjk", "ywec")
print is_anagram2("kelli", "illek")
print is_anagram2("sdfjk", "ywec")

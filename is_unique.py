def is_unique(str):
    for i in range(len(str)-1):
        for j in range(len(str)-1):
            if str[i] == str[i+1]:
                return False
    return True


print is_unique("kelli")
print is_unique("lmnop")
print is_unique("")

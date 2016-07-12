# Remove all the non-unique letters from a string, 
# keeping the remaining characters in order.

# "" --> ""
# "a" --> "a"
# "cat" --> "cat"
# "caat" --> "caat"

def unique_letters(str):

    unique_chars = []

    for char in str:
        if char not in unique_chars:
            unique_chars.append(char)

    print "".join(unique_chars)

unique_letters("a")
unique_letters("")
unique_letters("cat")
unique_letters("caat")


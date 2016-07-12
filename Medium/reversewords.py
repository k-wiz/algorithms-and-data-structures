

def reverse_string(str):
    """Reverses word-order in string, preserving spaces."""

    new_str = ""
    word = ""

    for char in str:
        if char != " ":
            word = word + char
        else:
            if word:
                new_str = word + new_str
                word = ""
            new_str = char + new_str
    new_str = word + new_str

    return new_str



str1 = "I love kelli"
str2 = " gotta  catch em all                "

print reverse_string(str1)
print reverse_string(str2)




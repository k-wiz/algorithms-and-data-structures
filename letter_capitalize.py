def letter_capitalize(str): 

    words = str.split(" ")
    new_str = []
    for word in words:
        word = word.replace(word[0], word[0].upper())
        new_str.append(word)

    return " ".join(new_str)


def LetterCapitalize(string): 
    result = []
    for word in string.split():
        result.append(word[0].upper() + word[1:])
    return result


print letter_capitalize("kelli is cool")
print letter_capitalize("oxford comma")
print LetterCapitalize("kelli is cool")
print LetterCapitalize("oxford comma")
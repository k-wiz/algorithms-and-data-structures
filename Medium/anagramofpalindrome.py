"""Is the word an anagram of a palindrome?

A palindrome is a word that reads the same forward and backwards
(eg, "racecar", "tacocat"). An anagram is a rescrambling of a word
(eg for "racecar", you could rescramble this as "arceace").

Determine if the given word is a re-scrambling of a palindrome.
The word will only contain lowercase letters, a-z.

Examples::

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False

"""
# 1. You want me to write afunction that takes in a string, and returns T/F depending on whether the string is an anagram of a palindrome?
# 2. Will I receive non-strings as input? What should I return if the string is empty? 
# 3. Test cases 
# 4. My strategy: a word is an anagram of a palindrome if each letter has a mate 
# (except for the middle letter, if odd number of letters). So, I'm going to iterate
# over the string, and count the ocurrences of each letter. The easiest way to do 
# that would be to use a dictionary. 
# 5. Pseudocode: for char in word: if char in dict, value += 1. Else add char to dict. 
# Then, if there is more than one odd value, return False. Else, return True. 

def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""

    letter_count = {}
    odd_count = 0

    # for char in word:
    #     if char in letter_count:
    #         letter_count[char] += 1
    #     else:
    #         letter_count[char] = 1

    for char in word:
        letter_count[char] = letter_count.get(char, 0) + 1

    for value in letter_count.values():
        if value % 2 != 0:
            odd_count += 1

    if odd_count > 1:
        return False
    return True




if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"

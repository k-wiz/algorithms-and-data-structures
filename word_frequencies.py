# Given a word doc, print words with their frequencies. 
# Now print the nth term in terms of frequency. 
  

def word_frequencies(string, n):

    # Remove punctuation (so word count is not skewed). 
    punctuation = ",.?!'"
    for char in punctuation:
        if char in string:
            string = string.replace(char, "")
    
    # Convert string into list of words, all lowercase, no newlines (so word count is not skewed).
    word_list = [word.lower().strip() for word in string.split(" ")]
    
    # Count occurrence of words. 
    word_count = {}

    for word in word_list:
        word_count[word] = word_count.get(word, 0) + 1

    # Find the word with the nth highest occurrence.
    # Get list of values. Return nth value. Get key with nth value. 
    nth_highest_freq = word_count.keys()[word_count.values().index(n+1)]


    return nth_highest_freq


str = """This technique is called Bubble Sort. Why? Because the big numbers 
bubble to the top! After the first pass through the list, the biggest number 
will be all the way to the right. After the second pass, the second highest 
number will be second from the right, and so on."""


print word_frequencies(str, 2)
def solution(S):
    # write your code in Python 2.7
    
    sentences = S.replace('?','.').replace('!','.').split('.')
    print sentences
    words = [sentence.strip().split(" ") for sentence in sentences]
    print words
    for word in words:
        word = word.remove('')
    longest_sentence = max(words, key=len)
    print longest_sentence
    
    return len(longest_sentence)

print solution("kelli. is   cool?")
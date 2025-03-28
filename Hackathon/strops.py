import string
from itertools import permutations
from collections import Counter
 
# get span of substring for a given word
def getspan(s, sub):
    span = []
    start = 0
    while True:
        start = s.find(sub, start)
        if start == -1:
            #print("substring not found")
            break
        end = start + len(sub)
        span.append((start, end))
        start += 1
    return len(span), span
 
 
# reversing a word
def reverseword(s):
    reverse_s = s[::-1]
    return reverse_s
 
 
#removing punctuation
def remove_punctuation(s):
    return ''.join([char for char in s if char not in string.punctuation])
 
 
#counting number of words
def count_words(s):
    words = s.split()
    return len(words)
 
 
# character mapping using dictionaries
def charactermap(s):
    return dict(Counter(s))
 
 
# convert string into title
def maketitle(s):
    return s.title()
 
 
#normalizing space
def normalize_space(s):
    return ' '.join(s.split())
 
 
#translating strings
def transform_string(s):
    return s[::-1].swapcase()
 
 
 
#permutations
def permut(s):
    return[''.join(p)for p in permutations(s)]
 
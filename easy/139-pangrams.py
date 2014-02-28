#####################################################################
# 
#        ORIGINAL PROBLEM:
#        Print whether or not a given string is a pangram, and the
#		 count of each letter in the string.
#
#        For more information, see the original prompt at 
#        http://www.reddit.com/r/dailyprogrammer/comments/1pwl73/11413_challenge_139_easy_pangrams/
#
#####################################################################
from __future__ import print_function
from collections import Counter
from string import lowercase

def is_pangram(sentence):
    c = Counter(sentence)
    for letter in lowercase:
        if c[letter] == 0:
            print("False", end='')
            break
    else:
        print("True", end='')
    for letter in lowercase:
        print(", {key}: {count}".format(key=letter, count=c[letter]), end='')
    print("")
        
if __name__ == "__main__":
    n = int(raw_input())
    sentences = (sentence.lower() for sentence in (raw_input() for x in xrange(n)))
    for sentence in sentences:
        is_pangram(sentence)
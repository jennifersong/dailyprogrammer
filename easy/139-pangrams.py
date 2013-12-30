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
import string

n = int(raw_input())
sentences = [sentence.lower() for sentence in (raw_input() for x in xrange(n))]
	
for current in sentences:
	c = Counter(current)
	is_pangram = True
	for letter in string.lowercase:
		if c[letter] == 0:
			is_pangram = False
			break
	print(is_pangram, end='')
	for letter in string.lowercase:
		print(", {key}: {count}".format(key=letter, count=c[letter]), end='')
	print("")
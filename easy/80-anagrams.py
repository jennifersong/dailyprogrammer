#####################################################################
# 
#        ORIGINAL PROBLEM:
#        Given a string, return all anagrams of that word (reading from a file).
#        BONUS: return the two largest "families" of anagrams in the file.
#
#        For more information, see the original prompt at 
#        http://www.reddit.com/r/dailyprogrammer/comments/x0v3e/7232012_challenge_80_easy_anagrams/
#
#####################################################################
import fileinput
from collections import Counter

def anagrams(word, file=fileinput.input()):
	return [line.strip() for line in file if sorted(line.strip().lower()) == sorted(word)
	 and line.strip().lower() != word]
		
def largest_family(file="enable1.txt"):
	f = open(file)
	content = f.readlines()
	sorted_content = Counter([''.join(sorted(word.strip())) for word in content])
	for each in sorted_content.most_common(2):
		print "{a}, {c}".format(a=anagrams(each[0], content), c=each[1])
		
print anagrams("triangle")
largest_family()
#####################################################################
# 
#        ORIGINAL PROBLEM:
#        Given an integer N and N strings, print the 90-degree
#		 string transpositions.
#
#        For more information, see the original prompt at 
#        http://www.reddit.com/r/dailyprogrammer/comments/1m1jam/081313_challenge_137_easy_string_transposition/
#
#####################################################################
import sys

n = int(raw_input())
wordList = [word for word in [raw_input() for x in range(n)]]
max_word = ""

# Add spacing to each word
for word in wordList:
	max_word = word if len(word) > len(max_word) else max_word
wordList = map(lambda word: word.ljust(len(max_word)), wordList)

for i in range(len(max_word)):
	for j in range(n):
		sys.stdout.write(wordList[j][i])		# not using print, due to extra space
	print "\n",
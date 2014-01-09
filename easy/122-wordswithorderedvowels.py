#####################################################################
# 
#        ORIGINAL PROBLEM:
#        Write a program that prompts the user to guess a randomly
#		 chosen integer between 1 and 100, inclusive.
#
#        For more information, see the original prompt at 
#        http://www.reddit.com/r/dailyprogrammer/comments/15ul7q/122013_challenge_115_easy_guessthatnumber_game/
#
#		 Of note, the one-line expression that will produce the same result if words = the word list:
#		 return filter(lambda x: re.findall('a{1}[^aeiouy]*e{1}[^aeiouy]*i{1}[^aeiouy]*o{1}[^aeiouy]*u{1}[^aeiouy]*y{1}[^aeiouy]*', x), words)
#
#####################################################################
import re

def contains_all_vowels(file):
	f = open(file)
	words = f.readlines() if f else None
	if words:
		for word in words:
			if re.sub('[^aeiouy]', '', word) == "aeiouy":
				print word.strip()
		
contains_all_vowels("../files/enable1.txt")
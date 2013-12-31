#####################################################################
# 
#        ORIGINAL PROBLEM:
#        Return true if a given string is only comprised of digits (0-9).
#
#        For more information, see the original prompt at 
#        http://www.reddit.com/r/dailyprogrammer/comments/12csk7/10302012_challenge_109_easy_digits_check/
#
#####################################################################
import string

def is_digits_only(strng):
	for letter in strng:
		if letter not in string.digits:
			return False
	return True
	
is_digits_only(raw_input())

# This function is for the purposes of codegolf only. It is significantly slower (O(n) minimum).
def is_digits_only_codegolf(strng):
	print all(map(lambda x: x in '0123456789', strng))
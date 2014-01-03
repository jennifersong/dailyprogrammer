#####################################################################
# 
#        ORIGINAL PROBLEM:
#        Given a string, return whether all brackets in the string are
#		 properly paired and ordered.
#
#        For more information, see the original prompt at 
#        http://www.reddit.com/r/dailyprogrammer/comments/11par4/10182012_challenge_104_intermediate_bracket_racket/
#
#####################################################################
import re

def are_brackets_paired(string):
	string = filter(lambda letter: letter in "[]{}()<>", string)
	while len(string) > 0:
		new_string = string
		for bracket in ["\[\]", "\{\}", "\(\)", "\<\>"]:
			string = re.sub(bracket, "", string)
		if new_string == string: 	# if equal, string has unmatchable bracket(s)
			return False
	return True
#####################################################################
# 
#        ORIGINAL PROBLEM:
#        Translate strings representing variable names into either 
#		 CamelCase, snake_case, or capitalized snake_case depending
#		 on the option provided as input.
#
#        For more information, see the original prompt at 
#        http://www.reddit.com/r/dailyprogrammer/comments/1q6pq5/11413_challenge_140_easy_variable_notation/
#
#####################################################################

operations = {
	'0': (lambda text: text[0][0] + "".join(map(lambda word: word.capitalize(), text))[1:]),		# CamelCase
	'1': (lambda text: "_".join(text)),																# snake_case
	'2': (lambda text: "_".join(map(lambda text: text.upper(), text)))								# CAPITALIZED_SNAKE_CASE
}

n, text = raw_input(), raw_input()
print "\n{n}\n{name}".format(n=n, name=operations[n](text.lower().split()))	
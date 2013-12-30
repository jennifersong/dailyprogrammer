#####################################################################
# 
#        ORIGINAL PROBLEM:
#        Given a string, find the longest substring that is comprised of
#		 two unique characters at maximum.
#
#        For more information, see the original prompt at 
#        http://www.reddit.com/r/dailyprogrammer/comments/1g0tw1/easy_longest_twocharacter_substring/
#
#		 The solution below runs in O(n) time at maximum.
#
#####################################################################
string = raw_input()
longest_str = []

x = 0
while x < len(string):
	first_char = string[x]		# first unique character
	second_char = ""			# second unique character
	current_str = []			# current string comprised of the two chars
	index = x					# where we are in the string
	while len(string) > index and (string[index] == first_char or \
	string[index] == second_char or second_char == ""):	
		current_str.append(string[index])
		if second_char == "" and string[index] != first_char:
			second_char = string[index]	# set second char if applicable
			next_index = index			# next loop should start at second char if exists
		index += 1
	# if no second char, rest of the string is one unique char so can skip checking
	# as a string of one unique char will always be inferior to two unique chars
	x = index if second_char == "" else next_index
	if len(current_str) >= len(longest_str):
		longest_str = current_str
print ''.join(longest_str)
		
#####################################################################
#       Original code follows. Runs in O(n**2) max time.
#####################################################################
# string = raw_input()
# longest_str = []
# for x in xrange(len(string)):
# 	first_char = string[x]		# first unique character
# 	second_char = ""			# second unique character
# 	current_str = []			# current string comprised of the two chars
# 	index = x					# where we are in the string
# 	while len(string) > index and (string[index] == first_char or \
# 	string[index] == second_char or second_char == ""):	
# 		current_str.append(string[index])
# 		if second_char == "" and string[index] != first_char:
# 			second_char = string[index]		# set second char if applicable
# 		index += 1
# 	if len(current_str) >= len(longest_str):
# 		longest_str = current_str

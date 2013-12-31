#####################################################################
# 
#        ORIGINAL PROBLEM:
#        Given ranges for two integers A and B, print all combinations
#		 of (A, B) where A*B is a palindrome.
#
#        For more information, see the original prompt at 
#        http://www.reddit.com/r/dailyprogrammer/comments/12csm4/10302012_challenge_109_intermediate/
#
#####################################################################
def is_palindrome(num_str):
	return num_str == num_str[::-1]
	
def is_product_palindrome(a_start, a_end, b_start, b_end):
	palindromes = []
	for a in xrange(a_start, a_end+1):
		for b in xrange(b_start, b_end+1):
			if is_palindrome(str(a*b)):
				palindromes.append((a, b))
	for palindrome in palindromes:
		print "{first}, {second}".format(first=palindrome[0], second=palindrome[1])
		
is_product_palindrome(1, 90, 1, 90)

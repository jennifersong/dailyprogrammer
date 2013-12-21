#####################################################################
# 
#        ORIGINAL PROBLEM:
#        Find the largest integer of a length of N digits that is
#		 evenly divisible by M.
#
#        For more information, see the original prompt at 
#        http://www.reddit.com/r/dailyprogrammer/comments/1jtryq/080613_challenge_134_easy_ndivisible_digits/
#
#####################################################################
n, m = map(int, raw_input().split())
numList = xrange(1, int(''.join(['1', '0' * n])))

for element in reversed(numList):
	if m > element:		# no answer so don't need to cycle through entire list
		break
	if element % m == 0:
		print element
		exit(0)
		
print "No solution found"
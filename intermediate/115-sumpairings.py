#####################################################################
# 
#        ORIGINAL PROBLEM:
#        Print all unique pairs (A, B) where A and B are members of a
#		 given array and A+B = C.
#
#		 Note that the solution below runs in O(n) time.
#
#        For more information, see the original prompt at 
#        http://www.reddit.com/r/dailyprogrammer/comments/15wm48/132013_challenge_115_intermediate_sumpairings/
#
#####################################################################
n = int(raw_input())
integers = map(int, raw_input().split())
c = int(raw_input())

found_pair = {}		# a number in this dict means that its pair has been found
for num in integers:
	other = c - num
	if num in found_pair:	# if it's in the dict, the pair isn't unique
		continue
	elif other in integers:		# (num + c - num) = c --> sum-pair
		found_pair[num] = True
		found_pair[other] = True	# add other to ensure uniqueness
		print "{num1}, {num2}".format(num1=num, num2=other)
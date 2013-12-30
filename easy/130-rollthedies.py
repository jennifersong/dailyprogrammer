#####################################################################
# 
#        ORIGINAL PROBLEM:
#        Given a string NdM representing an M-faced die rolled N times,
#		 print a space-delimited string representing each dice roll result.
#
#        For more information, see the original prompt at 
#        http://www.reddit.com/r/dailyprogrammer/comments/1givnn/061713_challenge_130_easy_roll_the_dies/
#
#####################################################################
import random

n, m = map(int, raw_input().split("d"))
random.seed()
print ' '.join([str(random.randrange(1, m+1)) for x in xrange(n)])
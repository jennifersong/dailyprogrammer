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

def roll_dice(n, m):
    print ' '.join((str(random.randrange(1, m+1)) for x in xrange(n)))

if __name__ == "__main__":
    n, m = (int(arg) for arg in raw_input().split("d"))
    random.seed()
    roll_dice(n, m)
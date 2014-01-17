#####################################################################
# 
#        ORIGINAL PROBLEM:
#        Given a string AdB(+/-)C representing a die notation, calculate
#        the value of a die roll with this notation.
#
#        For more information, see the original prompt at 
#        http://www.reddit.com/r/dailyprogrammer/comments/10pf0j/9302012_challenge_102_easy_dice_roller/
#
#####################################################################
import random, re

def roll_dice(die):
	splits = re.findall('(\d*)d(\d+)([\-\+]\d+)*', die)
	if not splits or len(splits[0][1]) == 0:
		return None
	a = int(splits[0][0]) if len(splits[0][0]) > 0 else 1
	b = int(splits[0][1])
	c = int(splits[0][2]) if len(splits[0][2]) > 0 else 0

 	return sum(random.randint(1, b) for x in xrange(a)) + c
	
print roll_dice(raw_input())
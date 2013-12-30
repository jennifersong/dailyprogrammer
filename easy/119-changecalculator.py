#####################################################################
# 
#        ORIGINAL PROBLEM:
#        Given an N amount of money in USD, round N to the nearest penny
#		 and print the minimum number of coins and those coins' denominations
# 		 needed to equal that amount of money. Includes bonus (do not print
#		 coins that are not used in the solution).
#
#        For more information, see the original prompt at 
#        http://www.reddit.com/r/dailyprogrammer/comments/17f3y2/012813_challenge_119_easy_change_calculator/
#
#		 NOTE: Getting the amount involves converting the input into a 
#		 Decimal object and converting that into an int instead of converting 
# 		 the string to a float and casting it into an int. This is due to the 
#		 faultiness of floating-point math (i.e. int(4.14 * 100) = 413).
#		 For more information, see the official Python documentation at:
#		 http://docs.python.org/3.3/tutorial/floatingpoint.html#tut-fp-issues
#
#####################################################################
from collections import OrderedDict
from decimal import ROUND_HALF_UP, Decimal
import math

amt = int(Decimal(raw_input()).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)*100)
all_coins = OrderedDict([("Quarters", 25), ("Dimes", 10), ("Nickels", 5), ("Pennies", 1)])

for (coin, value) in all_coins.items():
	count, amt = divmod(amt, value)
	if count > 0:
		print "{name}: {num}".format(name=coin, num=count)
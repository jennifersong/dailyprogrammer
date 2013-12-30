#####################################################################
# 
#        ORIGINAL PROBLEM:
#        Given an N-valued coin that converts to 3 coins of values N/2,
#		 N/3 and N/4, calculate the maximum value that can be received
#		 for that coin given an infinite number of allowable conversions.
#		 Does not include bonus.
#
#        For more information, see the original prompt at 
#        http://www.reddit.com/r/dailyprogrammer/comments/19rkqr/030613_challenge_121_intermediate_bytelandian/
#
#####################################################################
return_dict = {0: 0}

def max_value_return(coin):
	if coin not in return_dict:
		return_dict[coin] = max(max_value_return(coin/2) + max_value_return(coin/3) + max_value_return(coin/4), coin)
	return return_dict[coin]

coin = int(raw_input())
print max_value_return(coin)
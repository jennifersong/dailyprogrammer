#####################################################################
# 
#        ORIGINAL PROBLEM:
#        Given an N-valued coin that converts to 3 coins of values N/2,
#		 N/3 and N/4, calculate the number of 0-valued coins eventually
#		 received for that coin if all positive-valued coins are converted.
#
#        For more information, see the original prompt at 
#        http://www.reddit.com/r/dailyprogrammer/comments/19mn2d/030413_challenge_121_easy_bytelandian_exchange_1/
#
#####################################################################
return_dict = {0: 1}

def dp_perpetual_coin_return(coin):
	if coin not in return_dict:
		return_dict[coin] = dp_perpetual_coin_return(coin/2) + dp_perpetual_coin_return(coin/3) \
		 + dp_perpetual_coin_return(coin/4)
	return return_dict[coin]
	
print dp_perpetual_coin_return(int(raw_input()))

#####################################################################
#		 The code below does not use memoization, and is much slower.
#####################################################################
# def perpetual_coin_return(coin):
# 	return 1 if coin == 0 else perpetual_coin_return(coin/2) + perpetual_coin_return(coin/3) + perpetual_coin_return(coin/4)
# 	
# print perpetual_coin_return(int(raw_input()))
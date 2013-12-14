#####################################################################
# 
#	ORIGINAL PROBLEM:
#	Given two lists of N items and prices, print the items that have
#	changed in price and the amount that the price has changed per item.
#
#	For more information, see the original prompt at 
#	http://www.reddit.com/r/dailyprogrammer/comments/1sob1e/121113_challenge_144_easy_nuts_bolts/
#
#####################################################################

numItems = int(raw_input())

oldPrices = {item:int(price) for (item, price) in [raw_input().split(" ") for x in range(numItems)]}
newPrices = {item:int(price) for (item, price) in [raw_input().split(" ") for x in range(numItems)]}
	
for item in oldPrices:
	price = oldPrices.get(item) - newPrices.get(item)
	
	if price == 0:
		continue
	print "\n{item} {sign}{difference}".format(item=item, sign="+" if price > 0 else "", difference=price),
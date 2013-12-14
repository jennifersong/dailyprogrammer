numItems = int(raw_input())

oldPrices = {item:int(price) for (item, price) in [raw_input().split(" ") for x in range(numItems)]}
newPrices = {item:int(price) for (item, price) in [raw_input().split(" ") for x in range(numItems)]}
	
for item in oldPrices:
	price = oldPrices.get(item) - newPrices.get(item)
	
	if price == 0:
		continue
	print "\n{item} {sign}{difference}".format(item=item, sign="+" if price > 0 else "", difference=price),
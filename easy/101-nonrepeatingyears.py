#####################################################################
# 
#        ORIGINAL PROBLEM:
#        Given an inclusive range of years, count the number of years with no repeated digits.
#        BONUS: Count the number of years in the longest consecutive run of years with
#        repeated digits and years without repeated digits, from 1000 to 2013.
#
#        For more information, see the original prompt at 
#        http://www.reddit.com/r/dailyprogrammer/comments/10l8ay/9272012_challenge_101_easy_nonrepeating_years/
#
#####################################################################
def num_unrepeated_years(start, end):
	return len([x for x in xrange(start, end+1) if len(set(str(x))) == len(str(x))])
	
def longest_years(start, end):
	repeated = [x for x in xrange(start, end+1) if len(set(str(x))) == len(str(x))]
	unrepeated = [x for x in xrange(start, end+1) if len(set(str(x))) != len(str(x))]
	return longest_consecutive_years(unrepeated), longest_consecutive_years(repeated)
	
def longest_consecutive_years(years):
	longest, current = 0, 0
	for year in years:
		current = current + 1 if longest == 0 or year - previous == 1 else 1
		previous = year
		longest = current if current > longest else longest
	return longest

print num_unrepeated_years(1980, 1987)
print longest_years(1000, 2013)
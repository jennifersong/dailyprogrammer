#####################################################################
# 
#        ORIGINAL PROBLEM:
#        Verify that the unit test output is correct or incorrect as
#		 determined by the function used, the input and the output given.
#
#        For more information, see the original prompt at 
#        http://www.reddit.com/r/dailyprogrammer/comments/1fnutb/06413_challenge_128_easy_sumthedigits_part_ii/
#
#####################################################################
fn_dict = {
	'0': lambda x: x[::-1],
	'1': lambda x: x.upper()
}

n = int(raw_input())
strings = [x.split() for x in (raw_input() for y in range(n))]

for line in strings:
	print "Good test data" if fn_dict[line[0]](line[1]) == line[2] else \
	"Mismatch! Bad test data"
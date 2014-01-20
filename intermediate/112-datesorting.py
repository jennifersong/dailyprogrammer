#####################################################################
# 
#        ORIGINAL PROBLEM:
#        Given a file containing line-separated dates in the format "YYYY MM DD
#        hh:mm:ss", print these dates in chronological order from earliest to latest.
#        
#        For more information, see the original prompt at
#        http://www.reddit.com/r/dailyprogrammer/comments/137f87/11142012_challenge_112_intermediatedate_sorting/
#
#####################################################################
import sys

f = open(sys.argv[1])
if not f:
	exit(1)
for date in sorted(f):
	print date,
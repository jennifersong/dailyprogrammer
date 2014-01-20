#####################################################################
# 
#        ORIGINAL PROBLEM:
#        Given a string, print the string with all asterisks replaced,
#        as well as all characters bordering those asterisks.
#
#        For more information, see the original prompt at
#        http://www.reddit.com/r/dailyprogrammer/comments/12qi5b/1162012_challenge_111_easy_star_delete/
#
#####################################################################
import re
print re.sub(".?\*+.?", "", raw_input())
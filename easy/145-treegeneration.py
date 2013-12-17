#####################################################################
# 
#        ORIGINAL PROBLEM:
#        Draw an ASCII centered-triangle tree with a 1x3 character 
# 		 trunk and a base of N characters, reducing each row by 2 characters.
#
#        For more information, see the original prompt at 
#        http://www.reddit.com/r/dailyprogrammer/comments/1t0r09/121613_challenge_145_easy_tree_generation/
#
#####################################################################

vars = raw_input().split()
n, trunk, leaf = int(vars[0]), vars[1], vars[2]

for j in range(1, n+1, 2):
	print " " * ((n-j)/2), leaf * j
print " " * ((n-3)/2), trunk * 3
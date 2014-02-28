#####################################################################
# 
#        ORIGINAL PROBLEM:
#        Draw an ASCII centered-triangle tree with a 1x3 character 
# 	     trunk and a base of N characters, reducing each row by 2 characters.
#
#        For more information, see the original prompt at 
#        http://www.reddit.com/r/dailyprogrammer/comments/1t0r09/121613_challenge_145_easy_tree_generation/
#
#####################################################################
def generate_tree(n, trunk, leaf):
    for j in range(1, n+1, 2):
        print " " * ((n-j)/2), leaf * j
    print " " * ((n-3)/2), trunk * 3

if __name__ == "__main__":
    vars = raw_input().split()
    n, trunk, leaf = vars
    generate_tree(int(n), trunk, leaf)
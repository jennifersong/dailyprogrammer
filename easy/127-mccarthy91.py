#####################################################################
# 
#        ORIGINAL PROBLEM:
#        Write a program that prints out each step that McCarthy's function
#        will perform for a given integer N.
#
#        For more information, see the original prompt at 
#        http://www.reddit.com/r/dailyprogrammer/comments/1f7qp5/052813_challenge_127_easy_mccarthy_91_function/
#
#####################################################################

def mccarthy_91(n, num_times):
    if n > 100:
        print ("M(" * num_times) + str(n-10)+ (")" * num_times) + " since {n} is greater than 100".format(n=n)
        return n - 10
    else:
        print ("M(" * 2) + str(n+11) + (")" * 2) + " since {n} is equal to or less than 100".format(n=n)
        return mccarthy_91(mccarthy_91(n+11, 1), 0)
        
n = int(raw_input())
print "M({n})".format(n=n)
print mccarthy_91(n, 1)
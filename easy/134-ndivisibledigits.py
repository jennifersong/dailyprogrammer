#####################################################################
# 
#        ORIGINAL PROBLEM:
#        Find the largest integer of a length of N digits that is
#		 evenly divisible by M.
#
#        For more information, see the original prompt at 
#        http://www.reddit.com/r/dailyprogrammer/comments/1jtryq/080613_challenge_134_easy_ndivisible_digits/
#
#####################################################################
def largest_divisor(num_digits, divisor):
    numList = xrange(divisor, int(''.join(['1', '0' * num_digits])))
    for element in reversed(numList):
        if element % divisor == 0:
            print element
            return
    print "No solution found"

if __name__ == "__main__":
    n, m = (int(x) for x in raw_input().split())
    largest_divisor(num_digits = n, divisor = m)
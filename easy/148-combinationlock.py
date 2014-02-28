#####################################################################
# 
#        ORIGINAL PROBLEM:
#        Given the number of digits in a combination lock and the three
#		 digit-code, print the number of rotations needed to open the lock.
#
#        For more information, see the original prompt at 
#        http://www.reddit.com/r/dailyprogrammer/comments/1v4cjd/011314_challenge_148_easy_combination_lock/
#
#####################################################################
def clockwise(old, new, num_digits):
	return (new - old) % num_digits
	
def counterclockwise(old, new, num_digits):
	return (old - new) % num_digits
	
def full_rotation(num_digits):
	return num_digits

def combination_lock():
	digits = map(int, raw_input().split())
	n, first, second, third = digits

	total = full_rotation(n)*3 + clockwise(0, first, n) + \
	counterclockwise(first, second, n) + clockwise(second, third, n)
	return total

if __name__ == "__main__":
    print combination_lock()
#####################################################################
# 
#        ORIGINAL PROBLEM:
#        Sum the digits of an integer N, printing out each summation until
#        N is only one digit in length.
#
#        For more information, see the original prompt at 
#        http://www.reddit.com/r/dailyprogrammer/comments/1fnutb/06413_challenge_128_easy_sumthedigits_part_ii/
#
#####################################################################
def sum_digits(num):
    while len(str(num)) > 1:
        num = sum(int(digit) for digit in list(str(num)))
        print num
    
if __name__ == "__main__":
    num = raw_input()
    sum_digits(num)
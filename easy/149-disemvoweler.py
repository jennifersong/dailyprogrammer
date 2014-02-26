#####################################################################
# 
#        ORIGINAL PROBLEM:
#        Given a string, print two strings where the first string is the original string but with 
#        all vowels and spaces removed; and the second string is all vowels in the original string.
#
#        For more information, see the original prompt at 
#        http://www.reddit.com/r/dailyprogrammer/comments/1ystvb/022414_challenge_149_easy_disemvoweler/
#
#####################################################################
def disemvowel(strng):
    vowels = "aeiou"
    print ''.join(letter for letter in strng if letter not in vowels and letter not in " ")
    print ''.join(letter for letter in strng if letter in vowels)
    
if __name__ == "__main__":
    disemvowel(raw_input())
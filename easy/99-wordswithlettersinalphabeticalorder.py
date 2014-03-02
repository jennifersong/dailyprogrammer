#####################################################################
# 
#        ORIGINAL PROBLEM:
#        Given a list of words, return the number of words that have all
#        of their letters in alphabetical order (e.g. "ghost" but not "cab").
#
#        For more information, see the original prompt at 
#        http://www.reddit.com/r/dailyprogrammer/comments/101m7y/9172012_challenge_99_easy_words_with_letters_in/
#
#####################################################################
import fileinput

def is_alphabetized(string):
	return ''.join(sorted(string)) == string
	
if __name__ == "__main__":
    # Provide ../files/enable1.txt as a command-line argument for this to work.
    print len([word.strip() for word in fileinput.input() if is_alphabetized(word.strip())])
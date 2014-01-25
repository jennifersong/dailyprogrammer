#####################################################################
# 
#        ORIGINAL PROBLEM:
#        Given a string and a list of "exceptions", return the string
#        with all words capitalized except those in exceptions.
#        The first word of the string will always be capitalized.
#
#        For more information, see the original prompt at 
#        http://www.reddit.com/r/dailyprogrammer/comments/wjzly/7132012_challenge_76_easy_title_case/
#
#####################################################################
def titlecase(strng, exceptions):
	words = strng.lower().split()
	capitalized = [words[0].capitalize()]
	for word in words[1:]:
		capitalized.append(word.capitalize() if word not in exceptions else word)
	return " ".join(capitalized)
		
print titlecase('the quick brown fox jumps over the lazy dog', ['the', 'fox'])
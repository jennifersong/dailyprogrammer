#####################################################################
# 
#        ORIGINAL PROBLEM:
#        Given a fictional sport with a scoring system of (3, 6, 6+1, 6+2)
#		 point scores, print whether a given score is valid or invalid.
#
#        For more information, see the original prompt at 
#        http://www.reddit.com/r/dailyprogrammer/comments/1undyd/010714_challenge_147_easy_sport_points/
#
#####################################################################
from itertools import imap

possible_scores = [3, 6, 7, 8]
valid_dict = {}

def valid_score(score):
	if score not in valid_dict:
		if score < min(possible_scores):
			valid_dict[score] = False
		elif any(imap(lambda x: score % x == 0, possible_scores)):
			valid_dict[score] = True
		else:
			valid_dict[score] = any(imap(lambda x: valid_score(score-x), possible_scores))
	return valid_dict[score]

print "{v}alid Score".format(v="V" if valid_score(int(raw_input())) else "Inv")
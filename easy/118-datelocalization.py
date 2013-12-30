#####################################################################
# 
#        ORIGINAL PROBLEM:
#        Given a string that defines a certain mapping of characters to
#		 date and time amounts, replace those characters with the current
#	     date and times, leaving the rest of the string intact.
#
#        For more information, see the original prompt at 
#        http://www.reddit.com/r/dailyprogrammer/comments/16z9oj/012113_challenge_118_easy_date_localization/
#
#####################################################################

import datetime, re

s = raw_input()
now = datetime.datetime.now()

replacements = {
	"%l": None,			# must be calculated separately
	"%h": "%I",
	"%H": "%H",
	"%s": "%S",
	"%m": "%M",
	"%c": "%p",
	"%M": "%m",
	"%d": "%d",
	"%y": "%Y"
}

def replace_chars(to_replace):
	if to_replace == "%l":
		return str(now.microsecond / 1000)
	else:
		return now.strftime(replacements[to_replace])
		
for format_str, output in replacements.items():
	s = re.sub(format_str, replace_chars(format_str), s)
print s

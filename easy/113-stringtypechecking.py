#####################################################################
# 
#        ORIGINAL PROBLEM:
#        Given a string, print what "type" the string is. The program can distinguish 
#		 between int, float, date, and text strings. Monotype strings only.
#
#        For more information, see the original prompt at 
#        http://www.reddit.com/r/dailyprogrammer/comments/13hmz3/11202012_challenge_113_easy_stringtype_checking/
#
#####################################################################
int_digits = '0123456789+-'

fn_dict = {
	'date': (lambda strng: len(strng.split('-')) == 3),
	'float': (lambda strng: '.' in strng),
	'int': (lambda strng: all(map(lambda letter: letter in int_digits, strng))),
	'text': (lambda strng: not any([fn_dict['date'](strng), fn_dict['float'](strng), fn_dict['int'](strng)]))
}

def blue_steel(strng):
	for fn_type in fn_dict:
		if fn_dict[fn_type](strng):
			return fn_type
		
print blue_steel(raw_input())
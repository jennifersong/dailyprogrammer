#####################################################################
# 
#        ORIGINAL PROBLEM:
#        Given a text file *.txt, create a second file *_reversed.txt where
#        *_reversed.txt contains all lines and all words of *.txt, reversed.
#
#        For more information, see the original prompt at 
#        http://www.reddit.com/r/dailyprogrammer/comments/za9op/9032012_challenge_95_easy_reversing_text_in_file/
#
#####################################################################
from __future__ import print_function
import fileinput

poem = [' '.join(line.split()[::-1]) for line in fileinput.input()][::-1]
new_file_name = fileinput.filename().split(".")[0] + "_reversed.txt"
file = open(new_file_name, 'w')
for line in poem:
	print(line, file=file)
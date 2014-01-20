#####################################################################
# 
#        ORIGINAL PROBLEM:
#        Given a directory name, return the contents of all *.txt files in that directory.
#        BONUS: Support a -r flag to enable recursive operation through the subdirectories.
#
#        For more information, see the original prompt at 
#        http://www.reddit.com/r/dailyprogrammer/comments/11par4/10182012_challenge_104_intermediate_bracket_racket/
#
#####################################################################
import sys, os

directory = sys.argv[-1]
if not os.path.isdir(directory):
	print "Invalid directory: {dir}".format(dir=directory)
	exit(1)

def ls(walk):
	for root, subs, files in walk:
		print "DIRECTORY: {d}".format(d=root)
		txt_files = [file for file in files if ".txt" in file]
		for file in txt_files:
			file_path = os.path.join(root, file)
			print "=== {n} ({s} bytes)".format(n=file, s=os.path.getsize(file_path))
			print open(file_path).read()
				
if "-r" in sys.argv:
	ls(os.walk(directory))
else:
	ls(tuple([[directory, [], os.listdir(directory)]]))
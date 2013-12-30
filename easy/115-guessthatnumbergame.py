#####################################################################
# 
#        ORIGINAL PROBLEM:
#        Write a program that prompts the user to guess a randomly
#		 chosen integer between 1 and 100, inclusive.
#
#        For more information, see the original prompt at 
#        http://www.reddit.com/r/dailyprogrammer/comments/15ul7q/122013_challenge_115_easy_guessthatnumber_game/
#
#####################################################################
import random

random.seed()
num = str(random.randint(1, 100))

print "C> Please make a guess of a number in the range of 1 to 100 (inclusive)."
while True:
	guess = raw_input("U> ")
	if guess == "exit":
		print ":'("
		break
	else:
		if guess == num:
			print "C> Correct!"
			break
		else:
			try:
				print "C> Wrong. That number is too {adjective}.".format \
				(adjective="high" if int(guess) > int(num) else "low")
			except ValueError:
				print "C> That is not a number! Please guess only integers between 1 and 100!"
#####################################################################
# 
#	ORIGINAL PROBLEM:
#	Simulate the Monty Hall problem n times and print the win rate of
# 	two tactics (switching doors and keeping the original door).
#
#	For more information, see the original prompt at 
#	http://www.reddit.com/r/dailyprogrammer/comments/1qdw40/111113_challenge_141_easy_monty_hall_simulation/
#
#####################################################################

import random

outcomes = {}

n = int(raw_input())

def monty_hall(tactic):
	car, goat, goat2 = assignDoors()
	doors = [car, goat, goat2]
	choice = random.choice(doors)
	doors.remove(goat2 if choice == goat else goat)
	if tactic == '2': 		# switch doors
		choice = doors[0] if choice == doors[1] else doors[1]
	outcome = (choice == car)
	outcomes[outcome] = (outcomes[outcome] + 1) if outcomes.get(outcome) else 1

def assignDoors():
	goat = goat2 = car = random.randrange(1, 4)
	while goat == car:
		goat = random.randrange(1, 4)
		while goat2 == car or goat == goat2:
			goat2 = random.randrange(1, 4)
	return car, goat, goat2
	
for i in range(n):
	monty_hall('1')
print "Tactic 1 (sticking with initial choice): {percentage}% winning chance".format(percentage = (outcomes[True] / float(n) * 100))
outcomes = {}
for i in range(n):
	monty_hall('2')
print "Tactic 2 (switching doors): {percentage}% winning chance".format(percentage = (outcomes[True] / float(n) * 100))
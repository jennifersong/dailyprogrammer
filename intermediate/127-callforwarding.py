#####################################################################
# 
#        ORIGINAL PROBLEM:
#        Given a file representing a list of call forwarding setups and
#		 the days of setup, print the number of forwards in place for a
#		 given day and the longest forwarding chain.
#
#        For more information, see the original prompt at 
#        http://www.reddit.com/r/dailyprogrammer/comments/1g09qy/060913_challenge_127_intermediate_call_forwarding/
#
#####################################################################

n = int(raw_input())
records = [x.split() for x in (raw_input() for y in range(n))]
forwarding_directory = {}
is_chain_start = {}

day = int(raw_input())
day_forwards = []
for forward in records:
	if int(forward[2]) <= day and int(forward[2]) + int(forward[3]) - 1 >= day:	# if the forward was set up for that day
		day_forwards.append(forward[0])		# then add that to the list of forwards for that day
		forwarding_directory[forward[0]] = forward[1]	# and make a (number, receiver) dict

longest = 0
for forward in day_forwards:	# for each forward set up for that day:		
	current = forward			
	start = current				# used to check whether there is a loop
	chain = []					# list of forwards for this particular starting device
	while current in forwarding_directory:	# while current has another device to forward to:
		if current in is_chain_start:		
			break				# break if we know that current forward is circular
		chain.append(current)
		current = forwarding_directory[current]	# move to the next forwarded-to device
		if start == current:	# if there is a circular forward:
			is_chain_start[current] = True
			chain.append(current)
			print "Error: call forwarding chain detected: {chain}".format(chain=chain)
			break
	longest = len(chain) if len(chain) > longest else longest
	
print "{num} call forwardings set up on day {day}".format(num=len(day_forwards), day=day)
print "{num} call forwardings are the longest chain on day {day}".format(num=longest, day=day)
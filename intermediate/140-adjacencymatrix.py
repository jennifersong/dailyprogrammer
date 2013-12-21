#####################################################################
# 
#        ORIGINAL PROBLEM:
#        Print the adjacency matrix of a graph, given the graph's M
#		 lines of edge-node data.
#
#        For more information, see the original prompt at 
#        http://www.reddit.com/r/dailyprogrammer/comments/1t6dlf/121813_challenge_140_intermediate_adjacency_matrix/
#
#####################################################################
import sys

n, m = map(int, raw_input().split())
matrix = [n * [0] for x in range(n)]

for x in range(m):
	origin, dest = raw_input().split(" -> ")
	for node in origin.split():
		for end in dest.split():
			matrix[int(node)][int(end)] = 1

for row in matrix:
	for element in row:
		sys.stdout.write(str(element))
	sys.stdout.write("\n")
#####################################################################
# 
#        ORIGINAL PROBLEM:
#        Given a set of strings that represent edges and vertices in a graph,
#        print the edges in sorted order from leftmost to rightmost edge.
#
#        For more information, see the original prompt at 
#        http://www.reddit.com/r/dailyprogrammer/comments/1dsyrk/050613_challenge_124_easy_edge_sorting/
#
#####################################################################
n = int(raw_input())
edges = sorted([((x[1], x[2]), x[0]) for x in (raw_input().split() for y in range(n))])

print " ".join([edge[1] for edge in edges])
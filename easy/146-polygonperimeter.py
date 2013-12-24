#####################################################################
# 
#        ORIGINAL PROBLEM:
#        Calculate the perimeter of a polygon, given that it has N sides
#        and a circumradius of R (the distance between the center of the
#        polygon to any of its vertices).
#
#        For more information, see the original prompt at 
#        http://www.reddit.com/r/dailyprogrammer/comments/1tixzk/122313_challenge_146_easy_polygon_perimeter/
#
#####################################################################
import math

n, r = map(float, raw_input().split())
print round(n*r*2*math.sin(math.pi/n), 3)
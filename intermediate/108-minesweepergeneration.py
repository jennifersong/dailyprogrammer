#####################################################################
# 
#        ORIGINAL PROBLEM:
#        Given the length and width of a Minesweeper board and the number
#		 of mines in the board, generate a valid game of Minesweeper.
#
#        For more information, see the original prompt at 
#        http://www.reddit.com/r/dailyprogrammer/comments/126905/10272012_challenge_108_intermediate_minesweeper/
#
#####################################################################
import random

height, width, mines, mine, empty = 15, 15, 20, '*', '.'
board = [[empty for x in xrange(width)] for x in xrange(height)]
mine_locations = {}

# Print the board so it's pretty instead of using print board
def print_board():
	for row in board:
		print ''.join(row)
	
# Given a set of coordinates, return all valid neighbor coordinates.
def generate_number_coords(coords):
	x, y = coords[0], coords[1]
	coords_list = [(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x+1, y), \
	(x-1, y+1), (x, y+1), (x+1, y+1)]
	coords_list = filter(lambda (x, y): x > -1 and x < width \
	and y > -1 and y < height, coords_list)
	return coords_list

# Given a set of coordinates, return the number of surrounding mines.
def num_mines_around(coords):
	coords_list = generate_number_coords(coords)
	total_mines = 0
	for (x, y) in coords_list:
		if board[y][x] == mine:
			total_mines += 1
	return total_mines

# Set mines in board and mine locations.
while mines > 0:
	x, y = random.randrange(width), random.randrange(height)
	if (x, y) not in mine_locations:
		board[y][x] = mine
		mine_locations[(x, y)] = mines
		mines -= 1

# Set neighbors of mines to their "neighboring mines" values.		
for location in mine_locations:
	coords_list = generate_number_coords(location)
	for (x, y) in coords_list:
		if board[y][x] != mine:			# don't overwrite any surrounding mines
			board[y][x] = str(num_mines_around((x, y)))

print_board()
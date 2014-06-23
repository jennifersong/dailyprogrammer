#####################################################################
# 
#        ORIGINAL PROBLEM:
#        Simulate the game "Rock Paper Scissors Lizard Spock".
#
#        For more information, see the original prompt at 
#        http://www.reddit.com/r/dailyprogrammer/comments/23lfrf/4212014_challenge_159_easy_rock_paper_scissors/
#
#####################################################################
from random import randrange
from collections import defaultdict

valid_moves = ["rock", "paper", "scissors", "lizard", "spock"]
move_results = {"rock": {"paper": {"outcome": False, "text": "is covered by"}, "scissors": {"outcome": True, "text": "crushes"}, "lizard": {"outcome": True, "text": "crushes"}, "spock": {"outcome": False, "text": "is vaporized by"}}, 
"paper": {"rock": {"outcome": True, "text": "covers"}, "scissors": {"outcome": False, "text": "is cut by"}, "lizard": {"outcome": False, "text": "is eaten by"}, "spock": {"outcome": True, "text": "disproves"}}, 
"scissors": {"rock": {"outcome": False, "text": "is crushed by"}, "paper": {"outcome": True, "text": "is cut by"}, "lizard": {"outcome": True, "text": "decapitate"}, "spock": {"outcome": False, "text": "is smashed by"}}, 
"lizard": {"rock": {"outcome": False, "text": "is crushed by"}, "paper": {"outcome": True, "text": "eats"}, "scissors": {"outcome": False, "text": "is decapitated by"}, "spock": {"outcome": True, "text": "poisons"}}, 
"spock": {"rock": {"outcome": True, "text": "smashes"}, "paper": {"outcome": False, "text": "is disproven by"}, "scissors": {"outcome": True, "text": "smashes"}, "lizard": {"outcome": False, "text": "is poisoned by"}}}

def play_rpslp():
    player_move, computer_move = get_player_move(), get_computer_move()
    print "Player move: {p}\nComputer move: {c}\n".format(p=player_move, c=computer_move)
    if player_move == computer_move:
        print "Player ties with computer!"
        return "tie"
    else:
        result = move_results[player_move][computer_move]
        print "{p} {o} {c}! Player {w}!".format(p=player_move.capitalize(), o=result["text"], c=computer_move, w="wins" if result["outcome"] else "loses")
        return result["outcome"]
        
def calculate_stats(stats):
    total_games = float(sum(stats.itervalues()))
    print "Total games: {n}".format(n=int(total_games))
    print "Total wins: {n}; percentage: {p}%".format(n=stats[True], p=stats[True]/total_games*100)
    print "Total losses: {n}; percentage: {p}%".format(n=stats[False], p=stats[False]/total_games*100)
    print "Total ties: {n}; percentage: {p}%".format(n=stats["tie"], p=stats["tie"]/total_games*100)

def get_player_move():
    move = raw_input("\nEnter valid move for RPSLP: ").lower()
    if move in valid_moves:
        return move
    else:
        print "That is an invalid move! The valid moves are: {l}".format(l=valid_moves)
        return get_player_move()
        
def get_computer_move():
    return valid_moves[randrange(0, len(valid_moves))]

if __name__ == "__main__":
    stats = defaultdict(lambda: 0)
    result = play_rpslp()
    stats[result] += 1
    
    while raw_input("\nWould you like to play again? Enter yes to play again. Enter anything else to quit: ") == "yes":
        result = play_rpslp()
        stats[result] += 1
    calculate_stats(stats)
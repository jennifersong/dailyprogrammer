#####################################################################
# 
#        ORIGINAL PROBLEM:
#        Given the name of a move and the name of a Pokemon, print how effective
#		 the move will be based on type effectiveness.
#		 e.g. type_effect("Ice Beam", "Dragonite") = 4.
#		 e.g. type_effect("Earthquake", "Zapdos") = 0.
#		 e.g. type_effect("Flamethrower", "Dewgong") = 1.
#
#        For more information, see the original prompt at 
#        http://www.reddit.com/r/dailyprogrammer/comments/10pfsf/9302012_challenge_102_difficult_pok%C3%A9mon_types/
#
#####################################################################
import requests, re, string

def get_type_effectiveness(offense, defense):
	r = requests.get("http://pokemondb.net/type")
	matchups = re.findall("\<td title=\"([A-Za-z]+) &#8594; ([A-Za-z]+)\s=\s([A-Za-z]+)", r.text)
	effectiveness = {"super": 2, "normal": 1, "not": 0.5, "no": 0}
	return effectiveness[filter(lambda (o, d, e): (offense, defense) == (o, d), matchups)[0][2]]

def get_pokemon_types(pokemon):
	r = requests.get('http://pokemondb.net/pokedex/national')
	pokemon_data = re.findall(".*{p}.*".format(p=pokemon), r.text)
	if pokemon_data:
		type_data = re.findall("class=\"itype ([a-zA-Z]+)\"", pokemon_data[0])
		return map(lambda x: string.capitalize(str(x)), type_data)

def get_move_type(move):
	r = requests.get('http://pokemondb.net/move/all')
	type_data = re.findall(".*{m}.*".format(m=move), r.text)
	if type_data:
		move_data = re.findall("/type/([A-Za-z]+)\"", type_data[0])
		return string.capitalize(str(move_data[0]))

def type_effect(move, defending_pokemon):
	defensive_types = get_pokemon_types(defending_pokemon)
	move_type = get_move_type(move)
	if defensive_types and move_type:
		multiplier = 1
		for pokemon_type in defensive_types:
			multiplier *= get_type_effectiveness(move_type, pokemon_type)
		print multiplier
	
type_effect("Earthquakesdf", "Dewgong")
#####################################################################
# 
#        ORIGINAL PROBLEM:
#        Given a string, print all possible occurrences of a periodic
#        table element in the string, akin to the style of Breaking Bad.
#
#        For more information, see the original prompt at
#        http://www.reddit.com/r/dailyprogrammer/comments/z6o4k/9012012_challenge_94_easy_elemental_symbols_in/
#
#####################################################################
import requests, re

r = requests.get("http://www.lenntech.com/periodic/name/alphabetic.htm")
symbols = re.findall("http://www.lenntech.com/Periodic-chart-elements/(\w+)-en.htm", r.text)

def highlight_symbols(string):
	symbols_in = [str(sym) for sym in symbols if str(sym).lower() in string.lower()]	
	for symbol in symbols_in:
		print re.sub(symbol, "[" + symbol + "]", string, 1, re.IGNORECASE)

highlight_symbols(raw_input())
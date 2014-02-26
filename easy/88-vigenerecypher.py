#####################################################################
# 
#        ORIGINAL PROBLEM:
#        Implement the Vigenere cypher, both to encrypt and decrypt.
#
#        For more information, see the original prompt at 
#        http://www.reddit.com/r/dailyprogrammer/comments/y5sox/8132012_challenge_88_easy_vigen%C3%A8re_cipher/
#
#####################################################################
from math import ceil
from string import ascii_uppercase

def vigenere(strng, key, to_encrypt):
	encrypt = (key * int(ceil(float(len(strng)) / len(key))))[:len(strng)]
	op = 1 if to_encrypt else -1
	return "".join([ascii_uppercase[(ascii_uppercase.find(strng[x]) + 
		op * ascii_uppercase.find(encrypt[x])) % 26] for x in xrange(len(encrypt))])

# BONUS
strng, key = "HSULAREFOTXNMYNJOUZWYILGPRYZQVBBZABLBWHMFGWFVPMYWAVVTYISCIZRLVGOPGBRAKLUGJUZGLNBASTUQAGAVDZIGZFFWVLZSAZRGPVXUCUZBYLRXZSAZRYIHMIMTOJBZFZDEYMFPMAGSMUGBHUVYTSABBAISKXVUCAQABLDETIFGICRVWEWHSWECBVJMQGPRIBYYMBSAPOFRIMOLBUXFIIMAGCEOFWOXHAKUZISYMAHUOKSWOVGBULIBPICYNBBXJXSIXRANNBTVGSNKR", "BEGINNING"
print vigenere(strng, key, False)
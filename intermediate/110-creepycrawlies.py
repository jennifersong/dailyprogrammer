#####################################################################
# 
#        ORIGINAL PROBLEM:
#        Download the highest-rated 100 stories from the subreddit r/nosleep
#        and print them to standard output in plaintext.
#
#        For more information, see the original prompt at 
#        http://www.reddit.com/r/dailyprogrammer/comments/12k3xt/1132012_challenge_110_intermediate_creepy_crawlies/
#
#####################################################################
import requests

r = requests.get("http://www.reddit.com/r/nosleep/top.json?sort=top&t=all&limit=100")
for story in r.json()["data"]["children"]:
	print "=== " + story["data"]["title"] + " ==="
	print story["data"]["selftext"]
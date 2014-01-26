#####################################################################
# 
#        ORIGINAL PROBLEM:
#        Given the id of an imgur album and an output directory, save
#        all images in the album to the directory, where each image is
#        named {id}-{num} (id = album id; num = nth photo in the album).
#
#        For more information, see the original prompt at 
#        http://www.reddit.com/r/dailyprogrammer/comments/wk0jf/7132012_challenge_76_difficult_imgur_album/
#
#####################################################################
import requests, sys, re, os

album, directory = sys.argv[1], sys.argv[2]

r = requests.get("http://imgur.com/a/{id}/layout/blog".format(id=album))
img_list = enumerate(re.findall('div class="image" id="(\w+)"', r.text), 1)
if not os.path.exists(directory):
	os.makedirs(directory)
	
for img_tup in img_list:
	with open(directory + "/" + album + "-" + str(img_tup[0]) + ".jpg", 'wb') as f:
		 curr_img = requests.get("http://imgur.com/{img}.jpg".format(img=img_tup[1]))
		 for block in curr_img.iter_content():
			 if not block:
				 break
			 f.write(block)
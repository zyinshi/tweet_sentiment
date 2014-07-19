import sys
import math
import json
from collections import Counter


def computeFreq(fp):
	hash_tags = []
	cnt = 0
	for line in fp:
		par = json.loads(line)
		if(par.has_key('entities') and par.get('entities') and par.get('entities').get('hashtags')):
			hashobj = par.get('entities').get('hashtags')
			#print type(hashobj[0])
			hash_tags.append(hashobj[0]['text'].encode('utf-8'))
	#print hash_tags	
	for top_ten in Counter(hash_tags).most_common(10):
		print top_ten[0], top_ten[1]




def main():
	#sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[1])
	computeFreq(tweet_file)
	
	#lines(sent_file)
	#lines(tweet_file)

if __name__ == '__main__':
	main()

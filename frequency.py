import sys
import math
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    return len(fp)

def parseData(l):
	par = json.loads(l)
	tweet = par.get('text','')
	encoded_tweet = tweet.encode('utf-8')
	return encoded_tweet



def computeFreq(fp):
	all_terms = {}
	cnt = 0
	for line in fp:
		tweet_str = parseData(line)
		for word in tweet_str.split():
			all_terms[word] = all_terms.get(word, 0)+1
			#print word, "************",all_terms.get(word,0)
			cnt +=1
		#print cnt
		#print all_terms
	return all_terms, cnt





def main():
    #sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[1])
    freq_dict, count = computeFreq(tweet_file)
    for term in freq_dict.keys():
    	print '%s %.4f'%(term, float(freq_dict[term])/count)
    #hw()
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()

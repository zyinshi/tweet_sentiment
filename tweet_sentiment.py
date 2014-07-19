import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def buildDict(fp):
	scores = {}
	for line in fp:
		term, score = line.split("\t")
		scores[term] = int(score)
	return scores

def parseData(l):
	par = json.loads(l)
	tweet = par.get('text','')
	encoded_tweet = tweet.encode('utf-8')
	return encoded_tweet

	
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    tweet_text = tweet_file.readlines()
    tweet_score = []
    sentdict = buildDict(sent_file)
    for line in tweet_text:
    	tweet_str = parseData(line)
    	sum = 0
    	for word in tweet_str.split(" "):
    		sum = sum + sentdict.get(word, 0)
    	print sum
    

if __name__ == '__main__':
    main()

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

def buildDict(fp):
	scores = {}
	for line in fp:
		term, score = line.split("\t")
		scores[term] = int(score)
	return scores

def newDict(fp, dic):
	undefined_term = {}
	for line in fp:
		tweet_str = parseData(line)
		for word in tweet_str.split(" "):
			if(dic.has_key(word)==False):
				undefined_term[word]=[0,0,0]
	return undefined_term

def computeSent(fp, num_tweet, text_sent, terms):
	for i in range(num_tweet):
		tweet_str = parseData(fp[i])
		for word in tweet_str.split(" "): 
			if(terms.has_key(word)):
				terms[word][0] += text_sent[i]
				terms[word][1] += 1
				#print "*************", terms[word][0]
	for value in terms.values():
		#print value[0]
		if(value[1]==0):
			value[2]=0
		else:
			alpha = value[0]/value[1]
			value[2] = 5/(1+math.exp(-alpha))-0.5
	return terms








def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    tweet_text = tweet_file.readlines()
    line_num = lines(tweet_text)
    tweet_score = []
    sentdict = buildDict(sent_file)
    for line in tweet_text:
    	tweet_str = parseData(line)
    	sum = 0
    	for word in tweet_str.split(" "):
    		sum = sum + sentdict.get(word, 0)
    	tweet_score.append(sum)
    termdict = newDict(tweet_text, sentdict)
    new_dict = computeSent(tweet_text, line_num, tweet_score, termdict)

    for term in new_dict.keys():
    	print term, new_dict[term][2]
    
if __name__ == '__main__':
    main()

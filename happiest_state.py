import sys
import math
import json
from collections import defaultdict

states = {
		'AK': 'Alaska',
		'AL': 'Alabama',
		'AR': 'Arkansas',
		'AS': 'American Samoa',
		'AZ': 'Arizona',
		'CA': 'California',
		'CO': 'Colorado',
		'CT': 'Connecticut',
		'DC': 'District of Columbia',
		'DE': 'Delaware',
		'FL': 'Florida',
		'GA': 'Georgia',
		'GU': 'Guam',
		'HI': 'Hawaii',
		'IA': 'Iowa',
		'ID': 'Idaho',
		'IL': 'Illinois',
		'IN': 'Indiana',
		'KS': 'Kansas',
		'KY': 'Kentucky',
		'LA': 'Louisiana',
		'MA': 'Massachusetts',
		'MD': 'Maryland',
		'ME': 'Maine',
		'MI': 'Michigan',
		'MN': 'Minnesota',
		'MO': 'Missouri',
		'MP': 'Northern Mariana Islands',
		'MS': 'Mississippi',
		'MT': 'Montana',
		'NA': 'National',
		'NC': 'North Carolina',
		'ND': 'North Dakota',
		'NE': 'Nebraska',
		'NH': 'New Hampshire',
		'NJ': 'New Jersey',
		'NM': 'New Mexico',
		'NV': 'Nevada',
		'NY': 'New York',
		'OH': 'Ohio',
		'OK': 'Oklahoma',
		'OR': 'Oregon',
		'PA': 'Pennsylvania',
		'PR': 'Puerto Rico',
		'RI': 'Rhode Island',
		'SC': 'South Carolina',
		'SD': 'South Dakota',
		'TN': 'Tennessee',
		'TX': 'Texas',
		'UT': 'Utah',
		'VA': 'Virginia',
		'VI': 'Virgin Islands',
		'VT': 'Vermont',
		'WA': 'Washington',
		'WI': 'Wisconsin',
		'WV': 'West Virginia',
		'WY': 'Wyoming'
}

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
	tweet_content = tweet_file.readlines()

	tweet_score = []
	sentdict = buildDict(sent_file)
	for line in tweet_content:
		tweet_str = parseData(line)
		sum = 0
		for word in tweet_str.split(" "):
			sum = sum + sentdict.get(word, 0)
		tweet_score.append(sum)

	state_senti = defaultdict(lambda: 0)
	for i in range(len(tweet_content)):
		par = json.loads(tweet_content[i])
		if(par.has_key('place') and par.get('place')):
			addr = par['place']['full_name'].strip('!''@''/''~').encode('utf-8').split(', ')
			#print addr
			for pl in addr:
				#print len(addr), pl
				for brif, fname in states.items():
					if pl==fname or pl==brif:
						#print state_senti[brif]
						state_senti[brif] += tweet_score[i]
					
	happist = max(state_senti, key=state_senti.get)
	print happist
		
if __name__ == '__main__':
	main()





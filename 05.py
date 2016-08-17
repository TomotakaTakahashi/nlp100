#usage example:
#python3 05.py 2 "This is a pen."

import re
import sys

def n_gram(n, str):
	ngramList = {}
	n=int(n)
	str = str.lower()
	wordList=re.findall("[a-z]+",str)
	for word in wordList:
		if len(word) >= n:
			for i in range(len(word)-n+1):
				if word[i:i+n] in ngramList:
					ngramList[word[i:i+n]]+=1
				else:
					ngramList[word[i:i+n]]=1
	return ngramList

print (n_gram(sys.argv[1],sys.argv[2]))

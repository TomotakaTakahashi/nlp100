#usage example:
#python3 05.py 2 "This is a pen."

import re
import sys

# extract character n-grams and calculate n-gram frequency
def char_n_gram(n, str):
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


# extract character n-grams and calculate n-gram frequency 
def word_n_gram(n, str):
	next



if __name__ == '__main__':
	if len(sys.argv) != 3:
		print "Usage: %s <n> <sentence>" % (sys.argv[0])
		print "  <n>: n for n-gram."
		print "  <sentence>: input sentence to generate n-grams"
		print ""
		print "  e.g., %s 2 \"This is a pen.\"" % (sys.argv[0])
		exit(1)
		
	print (char_n_gram(sys.argv[1],sys.argv[2]))
	print (word_n_gram(sys.argv[1],sys.argv[2]))


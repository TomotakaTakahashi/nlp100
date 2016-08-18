str1="paraparaparadise"
str2="paragraph"

import re
import sys

# extract character n-grams and make the set
def char_n_gram(n, str):
	ngramSet = set()
	n=int(n)
	str = str.lower()
	wordList=re.findall("[a-z]+",str)
	for word in wordList:
		if len(word) >= n:
			for i in range(len(word)-n+1):
				ngramSet.add(word[i:i+n])
	return ngramSet

if __name__ == '__main__':
	X=char_n_gram(2,str1)
	Y=char_n_gram(2,str2)
	print("X=",X)
	print("Y=",Y)
	print("X&Y=",X&Y)
	print("X|Y=",X|Y)
	print("X-Y=",X-Y)
	print("Y-X=",Y-X)
	print("\"se\" in X :", "se" in X)
	print("\"se\" in Y :", "se" in Y)

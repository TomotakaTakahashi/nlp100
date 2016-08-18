#python3
import re
s="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
oneList=[1,5,6,7,8,9,15,16,19]

def extTwoFirstChar(str):
	return str[0:2]


wordList = re.findall("[a-zA-Z]+",s)
wordList=list(map(extTwoFirstChar, wordList))
for i in oneList:
	wordList[i-1]=wordList[i-1][0]


dict = {}
for i in range(len(wordList)):
	dict[wordList[i]]=i+1
# We often need to access an element of a list AND its index.
# Python provides a convenient function for this case, enumerate(list), that 
# returns (index, element) pair from the list.
# The code above can be rewritten as follows:
#
# for i,w in enumerate(wordList):
#	dict[w] = i+1
#

print(dict)

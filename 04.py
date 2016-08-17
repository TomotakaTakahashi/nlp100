#python3
import re
s="Hi He Lied Because Boron Could Not Oxidize Fluorin. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
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


print(dict)

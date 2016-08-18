import re

text="Test sentence."

def cipChar(match):
	return chr(219-ord(match.group()))


def cipher(s):	
	p=re.compile('[a-z]')
	res= p.sub(cipChar, s)
	return res


print(text)
print(cipher(text))
# to decode, execute cipher again


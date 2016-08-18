import re

text="Test sentence."

def cipChar(c):
	return chr(219-ord(c))


def cipher(s):	
	p=re.compile('[a-z]')
	res= p.sub(lambda x:cipChar(x.group()), s)
	return res


print(text)
print(cipher(text))
# to decode, execute cipher again


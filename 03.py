import re
s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
wordlist = re.findall("[a-zA-Z]+", s)
res = [len(word) for word in wordlist]

print(res)

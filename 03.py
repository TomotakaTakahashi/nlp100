import re
s="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
wordlist = re.findall("[a-zA-Z]+", s)
res = []
for word in wordlist:
  res += [len(word)]

print(res)

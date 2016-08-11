s="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
s=s.replace(',','')
s=s.replace('.','')
ss=s.split(' ')
res = []
for word in ss:
  res += [len(word)]

print(res)

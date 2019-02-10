import itertools

s0 = "パトカー"
s1 = "タクシー"
res = "".join(itertools.chain(*zip(s0, s1)))

print (res)

import re

text = "Test sentence."

def cip_char(c):
    return chr(ord('z') + ord('a') - ord(c)) # ord('a')+ord('z')=219


def cipher(s):
    p = re.compile('[a-z]')
    res = p.sub(lambda x: cip_char(x.group()), s)
    return res


print(text)
print(cipher(text))
# to decode, execute cipher again

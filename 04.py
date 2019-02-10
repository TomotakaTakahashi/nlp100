import re
s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. " \
    "New Nations Might Also Sign Peace Security Clause. Arthur King Can."
one_list = [1, 5, 6, 7, 8, 9, 15, 16, 19]

word_list = re.findall("[a-zA-Z]+", s)
word_list = [word[:min(2, len(word))] for word in word_list]
for i in one_list:
    word_list[i-1] = word_list[i-1][:1]

res = {}
for i, word in enumerate(word_list):
    res[word] = i+1

print(res)

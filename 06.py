import re

str1 = "paraparaparadise"
str2 = "paragraph"

# extract character n-grams and make the set
def char_n_gram(n, text):
    ngram_set = set()
    n = int(n)
    text = text.lower()
    word_list = re.findall("[a-z]+", text)
    for word in word_list:
        if len(word) >= n:
            for i in range(len(word) - n + 1):
                ngram_set.add(word[i: i+n])
    return ngram_set

if __name__ == '__main__':
    X = char_n_gram(2, str1)
    Y = char_n_gram(2, str2)
    print("X=", X)
    print("Y=", Y)
    print("X&Y=", X & Y)
    print("X|Y=", X | Y)
    print("X-Y=", X - Y)
    print("Y-X=", Y - X)
    print("\"se\" in X :", "se" in X)
    print("\"se\" in Y :", "se" in Y)

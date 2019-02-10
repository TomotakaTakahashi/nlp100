# usage example:
# python3 05.py 2 "This is a pen."

import re
import sys

# extract character n-grams and calculate n-gram frequency
def char_n_gram(n, text):
    ngram_list = {}
    n = int(n)
    text = text.lower()
    word_list = re.findall("[a-z]+", text)
    for word in word_list:
        if len(word) >= n:
            for i in range(len(word) - n + 1):
                if word[i: i + n] in ngram_list:
                    ngram_list[word[i: i+n]] += 1
                else:
                    ngram_list[word[i: i+n]] = 1
    return ngram_list


# extract character n-grams and calculate n-gram frequency
def word_n_gram(n, text):
    ngram_list = {}
    n = int(n)
    text = text.lower()
    word_list = re.findall("[a-z]+", text)
    num_of_words = len(word_list)
    for i in range(num_of_words - n + 1):
        ngram = ""
        for j in range(n):
            ngram += word_list[i + j]
            if j != n - 1:
                ngram += ' '
        if ngram in ngram_list:
            ngram_list[ngram] += 1
        else:
            ngram_list[ngram] = 1
    return ngram_list


if __name__ == '__main__':
    if len(sys.argv) != 1 + 2:
        exit(1)
    print(char_n_gram(sys.argv[1], sys.argv[2]))
    print(word_n_gram(sys.argv[1], sys.argv[2]))

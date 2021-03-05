from janome.tokenizer import Tokenizer
import pickle
import collections

t = Tokenizer()
words = []

with open("wagahai_list.pickle", mode="rb") as f:
    wagahai_list = pickle.load(f)

for sentence in wagahai_list:
    print(t.tokenize(sentence, wakati=True))

for text in wagahai_list:
    words += t.tokenize(text, wakati=True)
# 各単語の出現回数をカウント
c = collections.Counter(words)
print(c)
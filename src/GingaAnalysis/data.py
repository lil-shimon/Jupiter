import re
import pickle
from janome.tokenizer import Tokenizer
import collections

t = Tokenizer()
words = []

with open("../gingatetsudono_yoru.txt", mode="r", encoding="utf-8") as f:
    ginga_orignal = f.read()

ginga = re.sub("《[^》 ]+》", "", ginga_orignal)
# ginga = re.sub("[[^] ]", "", ginga)
ginga = re.sub("[| 　「」] ¥n", "", ginga)

separator = "。"
ginga_list = ginga.split(separator)
ginga_list.pop()
ginga_list = [x+separator for x in ginga_list]

with open("ginga_list.pickle", mode="wb") as f:
    pickle.dump(ginga_list, f)

with open("ginga_list.pickle", mode="rb") as f:
    ginga_list = pickle.load(f)

for sentence in ginga_list:
    words += t.tokenize(sentence, wakati=True)

c = collections.Counter(sentence)
print(c)

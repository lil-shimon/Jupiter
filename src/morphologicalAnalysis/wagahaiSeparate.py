from janome.tokenizer import Tokenizer
import pickle

t = Tokenizer()

with open("wagahai_list.pickle", mode="rb") as f:
    wagahai_list = pickle.load(f)

for sentence in wagahai_list:
    print(t.tokenize(sentence, wakati=True))
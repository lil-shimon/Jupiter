import re
import pickle
from janome.tokenizer import Tokenizer

# データの読み込み
# mode="r" == read
with open("./dataReform/wagahaiwa_nekodearu.txt", mode="r", encoding="utf-8") as f:
    wagahai_original = f.read()

wagahai = re.sub("《[^》 ]+》", "", wagahai_original)  # ルビを取り除く
wagahai = re.sub("[[^] ]", "", wagahai)  # 読みの注意の削除
wagahai = re.sub("[| 　「」] ¥n", "", wagahai)  # 全角、半角スペースの削除、 「」と改行の削除

separator = "。"  # 。をセパレーターにする
wagahai_list = wagahai.split(separator)  # セパレーターで文章を分けて、リストに入れる
wagahai_list.pop()  # 最後の要素は空白になるので削除
wagahai_list = [x + separator for x in wagahai_list]  # 文章の最後に。を追加

t = Tokenizer()
wagahai_words = []

for sentence in wagahai_list:
    wagahai_words.append(t.tokenize(sentence, wakati=True))

with open("wagahai_words.pickle", mode="wb") as f:
    pickle.dump(wagahai_words, f)

with open("wagahai_words.pickle", mode="rb") as f:
    wagahai_words = pickle.load(f)

    print(wagahai_words)
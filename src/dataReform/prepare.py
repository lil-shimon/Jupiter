import re
import pickle

# データの読み込み
# mode="r" == read
with open("wagahaiwa_nekodearu.txt", mode="r", encoding="utf-8") as f:
    wagahai_original = f.read()

print(wagahai_original)

wagahai = re.sub("《[^》 ]+》", "", wagahai_original)  # ルビを取り除く
wagahai = re.sub("[[^] ]", "", wagahai)  # 読みの注意の削除
wagahai = re.sub("[| 　「」] ¥n", "", wagahai)  # 全角、半角スペースの削除、 「」と改行の削除

print(wagahai)

separator = "。"  # 。をセパレーターにする
wagahai_list = wagahai.split(separator)  # セパレーターで文章を分けて、リストに入れる
wagahai_list.pop()  # 最後の要素は空白になるので削除
wagahai_list = [x + separator for x in wagahai_list]  # 文章の最後に。を追加

print(wagahai_list)

with open("../morphologicalAnalysis/wagahai_list.pickle", mode="wb") as f:  # pickleに保存
    pickle.dump(wagahai_list, f)

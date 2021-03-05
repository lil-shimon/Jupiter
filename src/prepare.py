import re

# データの読み込み
# mode="r" == read
with open("wagahaiwa_nekodearu.txt", mode="r", encoding="utf-8") as f:
    wagahai_original = f.read()

# print(wagahai_original)

wagahai = re.sub("《[^》 ]+》", "", wagahai_original)  # ルビを取り除く
wagahai = re.sub("[[^] ]", "", wagahai)  # 読みの注意の削除
wagahai = re.sub("[| 　「」] ¥n", "", wagahai) # 全角、半角スペースの削除、 「」と改行の削除

print(wagahai)

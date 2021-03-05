import re

# データの読み込み
# mode="r" == read
with open("wagahaiwa_nekodearu.txt", mode="r", encoding="utf-8") as f:
    wagahai_original = f.read()

print(wagahai_original)


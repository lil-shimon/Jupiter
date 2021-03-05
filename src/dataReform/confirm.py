import pickle

with open("../morphologicalAnalysis/wagahai_list.pickle", mode="rb") as f:
    wagahai_list = pickle.load(f)

print(wagahai_list)

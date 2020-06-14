from collections import Counter
import pickle

def get_counter(filename:str)->Counter:
    f = open(filename,"rb")
    data = pickle.load(f)
    f.close()
    all_hanjas = Counter()

    for key in data["annotated"]:
        assert isinstance(data[key][0][1],list), "list of annotated keys corrupted"
        for sentence in data[key]:
            all_hanjas += Counter(sentence[1])

    return all_hanjas





from collections import Counter
from konlpy.tag import Kkma
from nltk import ngrams
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

def trigram_getter(tagged_sentence:list)->Counter:
    stop = ["ETD","EPT","EFN","SF","JKO","EMO","JX","JC"]
    new_tag = tagged_sentence.copy()
    for tag in tagged_sentence:
        if tag[1].startswith("J") or tag[1].startswith("E") or tag[1].startswith("S"):
            new_tag.remove(tag)
    only_word = [tup[0] for tup in new_tag]
    return Counter(ngrams(only_word,3))


def trigram_analyze(word:str,dic:dict)->dict:
    trigrams_with_word = dict()
    for key in dic.keys():
        if word in key:
            trigrams_with_word[key] = dic[key]
    return trigrams_with_word




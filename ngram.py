import nltk
from konlpy.tag import Kkma
from urllib.request import urlopen
from urllib.parse import quote
import pickle
from pickle_helper import initialize
from collections import defaultdict
from nltk.lm import Laplace
from nltk.util import everygrams
from bs4 import BeautifulSoup
import re


def read_trigrams():
    training = []
    vocab = []
    text = []
    with open('trigrams.pkl', 'rb') as f:
        data = pickle.load(f)
        for d in data:
            trigrams = list(everygrams(d, max_len=3))
            training.append(trigrams)
            for word in d:
                vocab.append(word)
            text.append(d[0])
    return training, set(vocab), text

def read_sinko():
    known_list = []
    with open('known_sinko_list.pkl', 'rb') as f:
        data = pickle.load(f)
        for d in data:
            known_list.append(d)
    return known_list

def aux_delete(sentence, kkma):
    stop = ["ETD","EPT","EFN","SF","JKO","EMO","JX","JC"]
    tagged_sentence = kkma.pos(sentence)
    new_tag = tagged_sentence.copy()
    for tag in tagged_sentence:
        if tag[1].startswith("J") or tag[1].startswith("E") or tag[1].startswith("S"):
            new_tag.remove(tag)
    only_word = [tup[0] for tup in new_tag]
    return " ".join(only_word)

def ngram_model(train_data, vocab, n):
    model = Laplace(n)
    model.fit(train_data, vocab)
    return model

def search_def(word):
    defs = defaultdict(list)
    url = "https://hanja.dict.naver.com/search/word?query=" + quote(word)
    hanja = ''
    meaning = ''

    soup = BeautifulSoup(urlopen(url), 'lxml')
    hanja = soup.findAll("dt")
    meaning = soup.findAll("dd", {"class": "meaning"})
    for idx in range(len(meaning)):
        sent = aux_delete(meaning[idx].text, Kkma())
        if word not in sent and len(hanja[idx+3].text) == len(word):
            defs[hanja[idx+3].text] = re.sub("[\(\[\<].*?[\)\]\>]", "", sent)

    return defs

def find_closest_def(model, word, definitions):
    #print(model.score(word))
    #max_score = model.score(word, 'UNK') + model.score('UNK', word)
    max_count = 0
    max_def = ''
    max_hanja = ''
    for hanja, meaning in definitions.items():
        #score = 0
        count = 0
        for def_word in meaning.split():
            count += model.counts[[word]][def_word]
            #count += 1
            #score += model.score(word, def_word) + model.score(def_word, word)
        #if max_score < score/count:
        if max_count < count:
            max_count = count
            #max_score = score/count
            max_def = meaning
            max_hanja = hanja
    return word, max_hanja, max_count, max_def


known_list = read_sinko()
training, vocab, text = read_trigrams()
model = ngram_model(training, list(vocab), 3)
difficulty_list = []
for idx in range(len(text[:100])):
    #idx = idx + 2000
    if text[idx] in known_list:
        defs = search_def(text[idx])
        word, hanja, max_score, max_def = find_closest_def(model, text[idx], defs)
        if max_def != '':
            text[idx] = word + '(' + hanja + ')'
            difficulty_list.append(word + ' ' + hanja)            
            #print("test")
#print(" ".join(text))

file = open("results.txt", "w")
file.write(" ".join(text[:100]))
file.close()

file2 = open("difficulty_list.txt", "w", encoding='UTF-8')
for pair in difficulty_list:
    file2.write(pair+"\n")
file2.close()

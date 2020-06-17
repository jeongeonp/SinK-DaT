import nltk, re, pprint
from nltk.tokenize import word_tokenize
from urllib import request
from bs4 import BeautifulSoup
import pickle
from urllib.parse import urlencode, quote
import konlpy
from konlpy.tag import Okt


okt = Okt()


ROOT_URL = "http://korlex.pusan.ac.kr/search/WebApplication2/KorLex_SearchPage.aspx"

easy_vocab_list = []
with open('./TOPIC_vocab_list.csv', 'r') as csvfile:
    for line in csvfile.readlines():
        array = line.split(',')
        easy = array[1].split('0')[0]
        easy = easy.split('1')[0]
        easy_vocab_list.append(easy)

text_file = open("Textbook_middle.txt", "r")
text = text_file.read()
easy_corpus_list = text.split()

def preprocess_word(word):
    return okt.pos(word, stem=True)

def score_with_easy_list(word):
    if word in easy_vocab_list:
        return 1
    else:
        return 0

def score_with_easy_corpus(word):
    count = easy_corpus_list.count(word)
    print("score_with_easy_corpus : " + str(count))
    return int(count)   


def score_with_korlex(word):
    score = 0

    return score


def score_with_hanja_level(hanja):
    # hanja_enc = hanja.encode('gbk','strict')
    print("Scoring hanja " + hanja + "\n")
    score = 0
    url = "https://hanja.dict.naver.com/hanja?q=" + quote(hanja)
    soup = BeautifulSoup(request.urlopen(url).read(), 'html.parser')
    res = soup.find_all('a', href=True)
    found = False
    
    for a in res:
        if a['href'].startswith("/level/read/"):
            level = a['href'][12:][0]
            found = True
            print("The level of " + hanja + " is " + level + "\n")
    if not found:
        level = 0
        print(hanja + " has no level specified\n")
    return 10-level 

example_pairs = [('의사', '醫師'), ('학교', '學校')]

for pair in example_pairs:
    word, ch = pair
    stemmed = preprocess_word(word)[0][0]
    easy_score = score_with_easy_corpus(stemmed) + score_with_easy_list(stemmed)

        print(score_with_hanja_level(ch))
    if not easy_score:
        print(stemmed)
        print(score_with_hanja_level(ch))






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
with open('./TOPIC_vocab_list.csv', 'r', encoding='UTF-8') as csvfile:
    for line in csvfile.readlines():
        array = line.split(',')
        easy = array[1].split('0')[0]
        easy = easy.split('1')[0]
        easy_vocab_list.append(easy)

text_file = open("Textbook_middle.txt", "r", encoding='UTF-8')
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
    return int(count)   


def score_with_korlex(word):
    score = 0
    return score


def score_with_hanja_level(hanjas):
    # hanja_enc = hanja.encode('gbk','strict')
    score = 0
    for hanja in hanjas:
        url = "https://hanja.dict.naver.com/hanja?q=" + quote(hanja)
        soup = BeautifulSoup(request.urlopen(url).read(), 'html.parser')
        res = soup.find_all('a', href=True)
        found = False
        
        for a in res:
            if a['href'].startswith("/level/read/"):
                level = a['href'][12:][0]
                found = True
                # print("The level of " + hanja + " is " + level + "\n")
        if not found:
            level = 0
            # print(hanja + " has no level specified\n")
        score += int(level)
    return int(score / len(hanjas))

#example_pairs = [('의사', '醫師'), ('학교', '學校'), ('번뇌', '煩惱')]

all_pairs = []
file = open("difficulty_list.txt", "r", encoding='UTF-8')
for p in file.readlines():
    word_pair = p.split()
    all_pairs.append((word_pair[0], word_pair[1]))
file.close()

for pair in all_pairs:
    word, ch = pair
    stemmed = preprocess_word(word)[0][0]
    print("detected difficult word: " +  stemmed)
    print("level is " + str(score_with_hanja_level(ch)))
    #easy_score = score_with_easy_corpus(stemmed) + score_with_easy_list(stemmed)
    #if not easy_score:
    #    print("detected difficult word: " +  stemmed)
    #    print("level is " + str(score_with_hanja_level(ch)))






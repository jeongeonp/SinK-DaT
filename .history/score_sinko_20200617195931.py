import nltk, re, pprint
from nltk.tokenize import word_tokenize
from urllib import request
from bs4 import BeautifulSoup
import pickle
from urllib.parse import urlencode, quote


ROOT_URL = "http://korlex.pusan.ac.kr/search/WebApplication2/KorLex_SearchPage.aspx"

easy_list = []
with open('./TOPIC_vocab_list.csv', 'rb') as csvfile:
    for line in csvfile.readlines():
        array = line.split(',')
        easy_list.append(array[0])
# def fetch_option_data(symbol, datadate, expiration_date):
#     response = requests.get(ROOT_URL, params={"symbol": symbol, "datadate": datadate, "expirationDate": expiration_date})
#     return response.json()


# data = fetch_option_data('spx', '2018-06-01', '2018-06-15')

# for item in data:
#     print("AskPrice:", item['AskPrice'], "Last Price:", item["LastPrice"])

def get_ch(string):
    print(string)
    ans = [] #(char,num) num=0 for KOR // num=1 for CH // num=2 for ASCII(includes Eng alphabet) // num=3 for something else
    for char in string:
        num=0
        try:
            str_enc = char.encode('ascii','strict')
            num=2
        except:
            try:
                str_enc = char.encode('gbk','strict')
                num=1
            except:
                try:
                    str_enc = char.encode("euc_kr",'strict')
                    num=0
                except:
                    num=3
        ans.append((char,num))
    return ans 

def score_with_korlex(word):
    score = 0

    return score

def filter_easy(word):



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
        print(hanja + " has no level specified\n")
    # return score 

score_with_hanja_level('美')




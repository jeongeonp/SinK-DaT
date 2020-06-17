import nltk, re, pprint
from nltk.tokenize import word_tokenize
from urllib import request
from bs4 import BeautifulSoup


ROOT_URL = "http://korlex.pusan.ac.kr/search/WebApplication2/KorLex_SearchPage.aspx"


def fetch_option_data(symbol, datadate, expiration_date):
    response = requests.get(ROOT_URL, params={"symbol": symbol, "datadate": datadate, "expirationDate": expiration_date})
    return response.json()


data = fetch_option_data('spx', '2018-06-01', '2018-06-15')

for item in data:
    print("AskPrice:", item['AskPrice'], "Last Price:", item["LastPrice"])

def score_with_korlex(word):
    

    return score

def score_with_hanja_level(hanja):
    ROOT_URL = "https://hanja.dict.naver.com/hanja?q=" + hanja
    soup = BeautifulSoup(request.urlopen(ROOT_URL).read(), 'html.parser')
    res = soup.find_all('a', href=True)
    found = False
    
    for a in res:
        if a['href'].startswith("/level/read/"):
            level = a['href'][11:][0]
            found = True
            print("The level of " + hanja + " is" + level "\n")
    if not Found:
        print(hanja + " has no level specified\n")
    # return score 

score_with_hanja_level(美)


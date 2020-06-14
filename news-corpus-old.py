#http://srchdb1.chosun.com/pdf/i_archive/index.jsp?Y=1981&M=6&D=18

import nltk, re, pprint
from nltk.tokenize import word_tokenize
from urllib import request
from bs4 import BeautifulSoup
import pandas as pd
import random
from news-corpus-old import stack_data


def getTitleList(year, month, day):
    print("===== Searching [" + str(year) + "-" + str(month) + "-" + str(day) + "] =====\n")
    url = "http://srchdb1.chosun.com/pdf/i_archive/index.jsp?Y="+str(year)+"&M="+str(month)+"&D="+str(day)
    soup = BeautifulSoup(request.urlopen(url).read(), 'html.parser')
    res = soup.find_all('table')

    titleList = []

    for title in res:
        t = title.text.strip()
        if len(t) > 0:
            if ('•' == t[0]):
                titleList.append(t[1:].lstrip())

    return titleList

def show_example():
    # Year: 1945-1989, Month: 1-12, Day: 1-30 or 1-31
    result = getTitleList(1980, 1, 1)
    for r in result:
        print("**", r)
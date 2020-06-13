#http://srchdb1.chosun.com/pdf/i_archive/read_body.jsp?Y=1990&M=06&D=21&ID=9006210103

import nltk, re, pprint
from nltk.tokenize import word_tokenize
from urllib import request
from bs4 import BeautifulSoup
import pandas as pd
import random
import pickle


def getArticle(year, month, day):
    print("===== Searching [" + str(year) + "-" + str(month) + "-" + str(day) + "] =====\n")
    url = "http://srchdb1.chosun.com/pdf/i_archive/index.jsp?Y="+str(year)+"&M="+str(month)+"&D="+str(day)
    print(url)
    soup = BeautifulSoup(request.urlopen(url).read(), 'html.parser')
    res = soup.find_all('table')

    idList = []
    sentList = []

    for title in res:
        t = title.text.strip()
        if len(t) > 0:
            if ('•' == t[0]):
                print(t[1:].lstrip())
                idStart = str(title).find("ID=")
                idLen = str(title)[idStart:].find('"')
                id = str(title)[idStart:idStart+idLen]
                if (id != ""):
                    idList.append(id)

    print(idList)
    for i in idList:
        url = "http://srchdb1.chosun.com/pdf/i_archive/read_body.jsp?Y="+str(year)+"&M="+str(month)+"&D="+str(day)+"&"+i
        soup = BeautifulSoup(request.urlopen(url).read(), 'html.parser')
        article = soup.find_all('p')
        print('')
        print("*", i, ":", len(article))
        for p in article:
            p_split = nltk.sent_tokenize(p.text.strip())
            for s in p_split:
                sentList.append(s.replace("\n", ""))
    
    return sentList




# Year: 1990~, Month: 1-12, Day: 1-30 or 1-31
year = [1990,1991,1992,1993,1994,1995]
new_year = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]


result = getArticle(2005, 6, 15)

print(result)
#http://srchdb1.chosun.com/pdf/i_archive/read_body.jsp?Y=1990&M=06&D=21&ID=9006210103

import nltk, re, pprint
from nltk.tokenize import word_tokenize
from urllib import request
from bs4 import BeautifulSoup
import pandas as pd
import random
import pickle


def getArticle(year, month, day):
    # print("===== Searching [" + str(year) + "-" + str(month) + "-" + str(day) + "] =====\n")
    url = "http://srchdb1.chosun.com/pdf/i_archive/index.jsp?Y="+str(year)+"&M="+str(month)+"&D="+str(day)
    soup = BeautifulSoup(request.urlopen(url).read(), 'html.parser')
    res = soup.find_all('table')

    idList = []
    sentList = []

    for title in res:
        t = title.text.strip()
        if len(t) > 0:
            if ('•' == t[0]):
                # print(t[1:].lstrip())
                idStart = str(title).find("ID=")
                idLen = str(title)[idStart:].find('"')
                id = str(title)[idStart:idStart+idLen]
                if (id != ""):
                    idList.append(id)

    # print(idList)
    for i in idList:
        url = "http://srchdb1.chosun.com/pdf/i_archive/read_body.jsp?Y="+str(year)+"&M="+str(month)+"&D="+str(day)+"&"+i
        soup = BeautifulSoup(request.urlopen(url).read(), 'html.parser')
        article = soup.find_all('p')
        # print('')
        # print("*", i, ":", len(article))
        for p in article:
            p_split = nltk.sent_tokenize(p.text.strip())
            for s in p_split:
                sentList.append(s.replace("\n", ""))
    
    return sentList

def initialize(picklename):
    #DO NOT RUN THIS FUNCTION IF A FILE ALREADY EXISTS UNDER THE NAME "picklename"
    f = open(picklename,"wb")
    a = dict()
    pickle.dump(a,f)

# Year: 1990~, Month: 1-12, Day: 1-30 or 1-31

def stack_data(mode=0)->None:
    #check for existing data. keep them. start from earliest date that hasn't been mined yet. store the data in old.pkl after a day's over.
    assert int(mode) == 0 or int(mode) == 1, "mode should be either 0 (for old) or 1 (for new)"
    if mode ==0:
        try:
            data = pickle.load(open("old.pkl","rb"))
        except:
            print("old.pkl is not found. creating a new file.")
            data = dict()
        for year in range(1990,1995,1):
            for month in range(1,12,1):
                for day in range(1,31,1):
                    key = (year,month,day)
                    if not key in data.keys():
                        data[key] = getArticle(year,month,day)
                    print(key)
                    pickle.dump(data,open("old.pkl","wb"))
    if mode ==1:
        try:
            data = pickle.load(open("new.pkl","rb"))
        except:
            print("new.pkl is not found. creating a new file.")
            data = dict()
        for year in range(2010,2015,1):
            for month in range(1,12,1):
                for day in range(1,31,1):
                    key = (year,month,day)
                    if not key in data.keys():
                        data[key] = getArticle(year,month,day)
                    print(key)
                    pickle.dump(data,open("new.pkl","wb"))

def revivie_known_sinko():
    f = open("old.pkl","rb")
    data = pickle.load(f)[(1990,1,1)]
    f.close()
    the_set = set()
    for sent in data:
        the_set = the_set|set(sent[1])
    g = open("known_sinko_list.pkl","wb")
    pickle.dump(the_set,g)

# revivie_known_sinko()
stack_data()
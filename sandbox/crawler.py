import nltk
from urllib.request import urlopen
from urllib.parse import quote
import time
import requests
import html

def search():
    url = "http://newslibrary.chosun.com/view/article_view.html?id=2456719991231m1331&set_date=19991231&page_no=11"
    flag = False
    headers = {
        'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
        'referrer': 'https://google.com',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Pragma': 'no-cache'
    }
    response = requests.get(url,headers=headers)
    # with urlopen(url) as response:
    content = response.content

    for line in content.decode("utf-8").split("\n"):
        # line = line.decode('utf-8')
        if '<p id="subtitle1">' in line:
            print(line)
            flag = True
        if '</p>' in line:
            flag=False
        if flag: 
            print(line)

def search2():
    url = "http://srchdb1.chosun.com/pdf/i_archive/read_body.jsp?Y=1990&M=06&D=21&ID=9006210103"
    flag = False
    headers = {
        'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
    }
    response = requests.get(url,headers=headers)
    # with urlopen(url) as response:
    content = response.content

    for line in content.decode("euc-kr").split("\n"):
        # line = line.decode('utf-8')
        if '<p>' in line:
            print(line)
            flag = True
        if '</p>' in line:
            flag=False
        if flag: 
            print(line)

search()

        




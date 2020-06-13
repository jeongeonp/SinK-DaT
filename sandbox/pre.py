from bs4 import BeautifulSoup
import nltk
from konlpy.tag import Kkma
from urllib.request import urlopen
from urllib.parse import quote
#美 --> 미국
#타당하다 --> 마땅하다
#妥當하다 --> 타당하다 --> 마땅하다
kkma = Kkma()
# str1="妥當하다"
# str_enc = str1.encode('gbk','strict')
# print(str_enc)
# print(str_enc.decode('gbk','strict'))

def get_ch(string):
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

def collect_sinko(li):
    temp = ""
    ans = []
    prev = li[0][1]
    for item in li:
        if item[1]==prev:
            temp+=item[0]
        else:
            ans.append((temp,prev))
            temp=item[0]
            prev=item[1]
    ans.append((temp,prev))
    print(ans)

def naver_hanja(word):
    url = "https://hanja.dict.naver.com/search/word?query=" + quote(word)
    word = "<span><b>"+word+"</b></span>"
    with urlopen(url) as response:
        for line in response:
            line = line.decode("utf-8")
            if word in line:
                return True
    # url = urllib.request.urlopen(url)
    # print(url)

def get_sinko(tagged_sentence):
    #('이', 'MDT'), ('책', 'NNG'), ('은', 'JX'), ('매우', 'MAG'), ('타당', 'XR'), ('하', 'XSA'), ('다', 'EFN'), ('.', 'SF')]
    ans = []
    for tup in tagged_sentence:
        if naver_hanja(tup[0]): ans.append(tup[0])
    return ans

print("한자어 찾기")
str1='''기쁨을 만끽하다
'''
# print(kkma.pos(str1))
print(get_sinko(kkma.pos(str1)))
print("--------------------")
print("한자/영어로 된 말 찾기")
collect_sinko(get_ch("America는 한자어로 美國이라고 써요."))

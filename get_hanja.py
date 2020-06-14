import nltk
from konlpy.tag import Kkma
from urllib.request import urlopen
from urllib.parse import quote
import pickle
#美 --> 미국
#타당하다 --> 마땅하다
#妥當하다 --> 타당하다 --> 마땅하다

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

def naver_hanja(word, known_list):
    if word in known_list:
        return (True,known_list)
    url = "https://hanja.dict.naver.com/search/word?query=" + quote(word)
    text_word = word
    word = "<span><b>"+word+"</b></span>"
    with urlopen(url) as response:
        for line in response:
            line = line.decode("utf-8")
            if word in line:
                known_list.append(text_word)
                return (True,known_list)
    return (False,False)
    # url = urllib.request.urlopen(url)
    # print(url)

def get_sinko(sentence,kkma,known_list):
    #('이', 'MDT'), ('책', 'NNG'), ('은', 'JX'), ('매우', 'MAG'), ('타당', 'XR'), ('하', 'XSA'), ('다', 'EFN'), ('.', 'SF')]
    ans = []
    tagged_sentence = kkma.pos(sentence)
    for tup in tagged_sentence:
        nh_return = naver_hanja(tup[0],known_list)
        if nh_return[0]: 
            ans.append(tup[0])
            if nh_return[1]:
                known_list = nh_return[1]
    return ([sentence,ans],known_list)

def see_example():
    kkma = Kkma()
    print("한자어 찾기")
    str1='''식량과 자금을 지원하다.
    '''
    # print(kkma.pos(str1))
    print(get_sinko(kkma.pos(str1)))
    print("--------------------")
    print("한자/영어로 된 말 찾기")
    collect_sinko(get_ch("America는 한자어로 美國이라고 써요."))

def annotate_hanja(kkma):
    f = open("old.pkl","rb")
    data = pickle.load(f)
    f.close()

    f2 = open("known_sinko_list.pkl","rb")
    known_list = pickle.load(f2)
    f2.close()

    if "annotated" in data.keys():
        annotated = data["annotated"]
    else:
        annotated = []
    for key in data.keys():
        print("==================",key,"==================")
        if key in annotated: continue
        sentences = data[key]
        annotation = []

        l = len(sentences)
        count = 0

        for sent in sentences:
            hanja_tuple,known_list = get_sinko(sent,kkma,known_list)
            annotation.append(hanja_tuple)

            count +=1
            print(hanja_tuple)
            print(str(count)+"/"+str(l))
            
            g2 = open("known_sinko_list.pkl","wb")
            pickle.dump(known_list,g2)
            print(known_list)
            g2.close()

        data[key] = annotation
        annotated.append(key)
        data["annotated"] = annotated

        g = open("old.pkl","wb")
        pickle.dump(data,g)
        g.close()
        

def load_data(filename="old.pkl"):
    f = open(filename,"rb")
    data = pickle.load(f)
    f.close()
    return data

def store_data(filename,data):
    f = open(filename,"wb")
    pickle.dump(data,f)
    f.close()
    return data

#Data Organisation
#key = (1990,1,1), (1990,1,2) .... up to somewhere near 1990 september.
#value = list of 'sentence's
#sentence (annotated) = [raw_text, sinko_word_list]
#sentence (not annotated) = raw_text

#Special key = "annotation"  (not so special about it, it's just one key that's unlike other keys)
#Special value = (data["annotation"]) = list of dates(normal keys) for which sinko annotation has been made and stored.

    
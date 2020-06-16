import pickle
f = open("new.pkl","rb")
d = pickle.load(f)
f.close()


g = open("old.pkl","wb")
pickle.dump(d,g)
print(d.keys())
# from konlpy.tag import Kkma

# kkma = Kkma()
# sentence = "안중근 의사와 외과 의사는 좋은 사람이다."
# tagged_sentence = kkma.pos(sentence)
# print(tagged_sentence)
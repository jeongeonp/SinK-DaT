import pickle



g = open("trigrams.pkl","rb")
a = pickle.load(g)
print(a)
# from konlpy.tag import Kkma

# kkma = Kkma()
# sentence = "안중근 의사와 외과 의사는 좋은 사람이다."
# tagged_sentence = kkma.pos(sentence)
# print(tagged_sentence)
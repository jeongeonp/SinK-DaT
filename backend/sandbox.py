
from konlpy.tag import Kkma
txt = "교수님, 과제가 극도로 많아 삶에 상당한 무기력감을 느끼고 있습니다."
kkma = Kkma()
tagged_sentence = kkma.pos(txt)
print(tagged_sentence)
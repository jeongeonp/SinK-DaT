import pytest
from backend.counter import *

def test_always_pass():
    assert 1==1

def test_get_counter():
    all_hanjas = get_counter("backend/old.pkl")
    assert isinstance(all_hanjas, dict), "all hanjas was not dictionary form."
    for key, value in all_hanjas.items():
        assert isinstance(key,str), "storage at old.pkl was not annotated. probably not correctly initialised?"
        assert isinstance(value,int), "returned dictionary is not Counter form"

def test_trigram_getter():
    txt = [('교수님', 'NNG'), (',', 'SP'), ('과제', 'NNG'), ('가', 'JKS'), ('극도', 'NNG'), ('로', 'JKM'), ('많', 'VA'), ('아', 'ECD'), ('삶', 'NNG'), ('에', 'JKM'), ('상당', 'NNG'), ('하', 'XSV'), ('ㄴ', 'ETD'), ('무기력', 'NNG'), ('감', 'NNG'), ('을', 'JKO'), ('느끼', 'VV'), ('고', 'ECE'), ('있', 'VXV'), ('습니다', 'EFN'), ('.', 'SF')] 
    trigrams = trigram_getter(txt)
    assert isinstance(trigrams,dict), "acquired trigram is not dictionary form."
    for key, value in trigrams.items():
        assert len(key)==3, "trigrams contain something that is not trigram"
        for word in key:
            assert isinstance(word,str), "trigrams contain non string object"
        assert isinstance(value,int), "trigrams are not in counter form"

def test_trigram_analyze():
    txt = [('교수님', 'NNG'), (',', 'SP'), ('과제', 'NNG'), ('가', 'JKS'), ('극도', 'NNG'), ('로', 'JKM'), ('많', 'VA'), ('아', 'ECD'), ('삶', 'NNG'), ('에', 'JKM'), ('상당', 'NNG'), ('하', 'XSV'), ('ㄴ', 'ETD'), ('무기력', 'NNG'), ('감', 'NNG'), ('을', 'JKO'), ('느끼', 'VV'), ('고', 'ECE'), ('있', 'VXV'), ('습니다', 'EFN'), ('.', 'SF')] 
    trigrams = trigram_getter(txt)
    gyosu = trigram_analyze("교수님",trigrams)
    assert isinstance(gyosu,dict), "trigram with specified word did not return dictionary form"
    assert "교수님" in list(gyosu.keys())[0], "trigram didnot contain the specified word"

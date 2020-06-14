from news-corpus-new import *
from news-corpus-old import *

def initialize(picklename):
    #DO NOT RUN THIS FUNCTION IF A FILE ALREADY EXISTS UNDER THE NAME "picklename"
    f = open(picklename,"wb")
    a = dict()
    pickle.dump(a,f)

# Year: 1990~, Month: 1-12, Day: 1-30 or 1-31

def stack_data(filename:str,getter:FUNCTION)->None:
    #check for existing data. keep them. start from earliest date that hasn't been mined yet. store the data in old.pkl after a day's over.
    try:
        data = pickle.load(open(filename,"rb"))
    except:
        print("filename '", filename, "' is not found. creating a new file.")
        data = dict()
    for year in range(1990,1995,1):
        for month in range(1,12,1):
            for day in range(1,31,1):
                key = (year,month,day)
                if not key in data.keys():
                    data[key] = getter(year,month,day)
                pickle.dump(data,open(filename,"wb"))
                print(key)


def revivie_known_sinko():
    f = open("old.pkl","rb")
    data = pickle.load(f)[(1990,1,1)]
    f.close()
    the_set = set()
    for sent in data:
        the_set = the_set|set(sent[1])
    g = open("known_sinko_list.pkl","wb")
    pickle.dump(the_set,g)

import pickle
def initialize(picklename):
    #DO NOT RUN THIS FUNCTION IF A FILE ALREADY EXISTS UNDER THE NAME "picklename"
    f = open(picklename,"wb")
    a = dict()
    pickle.dump(a,f)

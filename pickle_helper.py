import pickle

def initialize(picklename):
    #DO NOT RUN THIS FUNCTION IF A FILE ALREADY EXISTS UNDER THE NAME "picklename"
    f = open(picklename,"wb")
    a = dict()
    pickle.dump(a,f)

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
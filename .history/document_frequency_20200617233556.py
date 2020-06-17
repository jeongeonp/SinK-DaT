from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)
        text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text

def check_frequency(word, text):
    count1 = text1.split().count(word)

    return count1, count2    

text = convert_pdf_to_txt('Textbook_middle.pdf')
text_file = open("Textbook_middle.txt", "w")
text_file.write(text)
text_file.close()
print(check_frequency('개념', text))



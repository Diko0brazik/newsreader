
import requests_html
from requests_html import HTMLSession
import psycopg2
from collections import OrderedDict
import re
from writetobasetxt import base
from datetime import datetime, timezone


#table id slovo
#table type news, id chastota
#table nametable type news
#https://habr.com/ru/post/349860/

def main():
    #txt = 'ПРивет аопр лдов. ываыва! ываыва ываыва fgh fgh '
    #txt = readtext('Путеводитель по миру паранормальных явлений.fb2')
     
    txt = readInvestingcom()
    #di = countWordsInTxt(txt)
    #writeToBase(di)
    #di = {"te":34, 're':32 }
    #writeToBase(di)
    return(None)



def readInvestingcom():
    b = base()
    session = HTMLSession()    
    baseurl = 'https://www.investing.com/news/'
    sections = ('cryptocurrency-news', 'stock-market-news', 'commodities-news', 
                'forex-news', 'economy', 'economic-indicators', 'general', 'world-news',
                'politics', 
            ) 
    for section  in sections:
        txt = []    
        for i in range(1,10):
            url = f'{baseurl}{section}/{str(i)}'
            txt.extend(getAPtegs(session.get(url)))
        txt = ' '.join(txt)
        #================ write base
        b.writetobasetxt(txt, 'investing.com', section)
    return(txt)


def getAPtegs(r):
    aa = r.html.find('a')
    ps = r.html.find('p')
    txt = [a.attrs['title'].lower() for a in aa if 'title' in a.attrs]
    txt2 = [a.attrs['title'].lower() for a in ps if 'title' in a.attrs]
    txt3 = [p.text.lower() for p in ps if not p.text == '']
    txt.extend(txt2)
    txt.extend(txt3)
    return(txt)












def readtext(fname="text.txt"): # delete
    with open(fname, encoding="utf-8") as f: #errors="ignore"
        txt = f.read()
    return(txt)

if __name__ == "__main__":
    main()
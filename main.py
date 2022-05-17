import requests_html
from requests_html import HTMLSession
import psycopg2
from collections import OrderedDict
import re



#table id slovo
#table type news, id chastota
#table nametable type news
#https://habr.com/ru/post/349860/

def main():
    #txt = 'ПРивет аопр лдов. ываыва! ываыва ываыва fgh fgh '
    #txt = readtext('Путеводитель по миру паранормальных явлений.fb2')
    
    txt = readInvestingcom()
    di = countWordsInTxt(txt)
    writeToBase(di)
    #di = {"te":34, 're':32 }
    #writeToBase(di)
    return(None)

def readInvestingcom():
    session = HTMLSession()
    urls = ('https://www.investing.com/news/cryptocurrency-news/',) 
    txt = []                                           
    for url in urls:
        for i in range(1,10):
            urlwithnumber = url+str(i)
            txt.extend(getAPtegs(session.get(urlwithnumber)))
    txt = ' '.join(txt)
    return(txt)


def getAPtegs(r):
    aa = r.html.find('a')
    ps = r.html.find('p')
    txt = [a.attrs['title'] for a in aa if 'title' in a.attrs]
    txt2 = [a.attrs['title'] for a in ps if 'title' in a.attrs]
    txt3 = [p.text for p in ps if not p.text == '']
    txt.extend(txt2)
    txt.extend(txt3)
    return(txt)




def writeToBase(di):
    conn = psycopg2.connect(dbname='newswords', user='newswords', 
                            password='123',     host='localhost')
    conn.autocommit = True
    c = conn.cursor()
    li = [(i,di[i]) for i in di ]
    c.executemany(''' insert into test (word, count) values(%s,%s) ''', li)
    
    
    pass




def countWordsInTxt(txt=None):
    #return dict     word:count
    #txt = 'ПРивет аопр лдов. ываыва! ываыва ываыва fgh fgh '
    lt = re.findall(r'\w+', txt)
    #lt = re.finditer(r'\w+', txt)
    #lt = re.split(r'\b', txt)
    r = {}
    di = OrderedDict.fromkeys(lt)
    pass
    #li = [i for n, i in enumerate(lt) if i not in lt[:n]]
    #print(len(lt), "   ", len(li))
    k=0
    for i in di:
        #s = i #.group()
        pass
        di[i]=txt.count(i)
        #if not s in r:
        #    r.update({s: txt.count(s)})
        k=k+1
    #print(r)
    #print(lt)
    return(di)

def readtext(fname="text.txt"):
    with open(fname, encoding="utf-8") as f: #errors="ignore"
        txt = f.read()
    return(txt)

if __name__ == "__main__":
    main()
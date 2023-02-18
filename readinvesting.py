from requests_html import HTMLSession
from collections import OrderedDict
from writetobasetxt import base
from datetime import datetime, timezone

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
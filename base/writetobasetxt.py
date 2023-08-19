import psycopg2
import re
from datetime import datetime, timezone
from collections import OrderedDict
import old.dbconnect as dbconnect

def main():
    txt = 'fg fg sdddddd'
    b = base()
    b.writetobasetxt(txt, 'test.site', 'test.section')
    pass

# def writetobasetxt(txt,  site, sectionOfSite, date, base = None):
#     di = countWordsInTxt(txt)
#     writeToBase(di, site, sectionOfSite, date, base)



class base():

    def __init__(t):
        t.conn = dbconnect.conn()
        t.conn.autocommit = True
        t.date = datetime.now(timezone.utc)
        t.basename = 'words'

    def countWordsInTxt(t, txt=None):
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



    #====================================== write to base =================
    def writetobasetxt(t, txt, site, sectionOfSite):
        date=t.date
        basename = t.basename
        di = t.countWordsInTxt(txt)
        c = t.conn.cursor()
        li = [(i, di[i], date, site, sectionOfSite) for i in di ]
        print(f'''write to base {len(li)} rows, date: {date.strftime("%Y-%m-%d, %H:%M")}, 
                                site: {site}, section: {sectionOfSite}''')
        c.executemany(f''' insert into {basename} (word, count, timestamp, site, section) values(%s,%s,%s,%s,%s) ''', li)









if __name__ == "__main__":
    main()
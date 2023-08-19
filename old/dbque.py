import old.dbconnect as dbconnect

def main():
    words()
    #c=dbconnect.connect5().cursor()
    #dd(c)

def words():
    c = dbconnect.cursor()
    q = '''
    select word 
    from words 
    group by word
    '''
    c.execute(q)
    ret = [map(c)]
    return(ret)   

    # how many times pputed data in one hour with same site and sector of site
def dd(c): 
    #site = 
    #section = 
    q = '''
    SELECT timestamp, site
    FROM words

    GROUP BY timestamp, site


    '''
    pr(c, q)



    

def pr(c, q):
    c.execute(q)
    # row = c.fetchone()
    # while row is not None:
    #     print(row)
    #     row = cursor.fetchone()

    for row in c:
        print(row)



if __name__ == '__main__':
    main()

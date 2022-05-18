import psycopg2


def main():

    conn = psycopg2.connect(dbname='newswords', user='newswords', 
                                    password='123',     host='localhost')
    conn.autocommit = True
    c = conn.cursor()

    sql = ''' select word from words group by word '''
    c.execute(sql)
    raw = c.fetchall()
    rawwords = [x[0] for x in raw]
    c.execute(''' select word from dictionary  ''')
    raw = c.fetchall()
    dictionary = [x[0] for x in raw]    
    for word in rawwords:
        if not word in dictionary:
            c.execute(''' insert into dictionary (word) values(%s) ''', (word,) )


    
    pass






if __name__ == "__main__":
    main()
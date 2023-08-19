import psycopg2


def main():

    conn = psycopg2.connect(dbname='newswords', user='newswords', 
                                    password='123',     host='localhost')
    conn.autocommit = True
    c = conn.cursor()

    sql = ''' select word, sum(count) c from words where timestamp between '2022-05-18' and '2022-05-19' 
    group by word order by c desc''

    c.execute(sql)
    r = c.fetchall()

    '''

    pass






if __name__ == "__main__":
    main()
from tkinter.tix import Tree
import psycopg2

def main():
    pass

def cursor():
    cn = conn()
    cn.autocommit(True)
    return(cn.cursor())

def conn():
    return(connect5())
    return(connectlocal())


def connect5():
    conn = psycopg2.connect(dbname='newswords', user='newswords', 
                                password='123',     host='10.0.0.5')
    return(conn)
    pass

def connectlocal():
    conn = psycopg2.connect(dbname='newswords', user='newswords', 
                                password='123',     host='localhost')
    return(conn)
    pass

if __name__ == "__main__":
    main()
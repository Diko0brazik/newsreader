import psycopg2
import old.dbconnect as dbconnect

def main():
    conn = dbconnect.conn()
    # conn = psycopg2.connect(dbname='postgres', user='postgres', 
    #                                 password='123',     host='localhost')
    conn.autocommit = True
    c = conn.cursor()
    c.execute(

'''
CREATE TABLE public.words
(
    word text,
    count bigint,
    "timestamp" timestamp with time zone,
    site text,
    section text
);

ALTER TABLE IF EXISTS public.words
    OWNER to newswords;'''
    )

    
    
    
    
    c.execute(
'''
CREATE TABLE public.dictionary
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 ),
    word text
);

ALTER TABLE IF EXISTS public.dictionary
    OWNER to newswords;
'''
    )


if __name__ == "__main__":
    main()
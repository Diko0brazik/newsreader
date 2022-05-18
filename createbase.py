import psycopg2

def main():
    pass


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


'''
CREATE TABLE public.dictioanry
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 ),
    word text
);

ALTER TABLE IF EXISTS public.dictionary
    OWNER to newswords;
'''

if __name__ == "__main__":
    main()
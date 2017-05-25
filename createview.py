import psycopg2
"""Import the psycopg  adapter to allow intergration with PostgreSQL database
and the below python code"""

DBNAME = "news"


def one():
    """Returns a list most popular articles, their author, and respective
    count from newsdata.sql  """
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute("create view one as select * from log limit 1")
        return c.fetchall()
        print("fetchall ran")
        db.close()
    
    except:
        print("function didn't run")


one()
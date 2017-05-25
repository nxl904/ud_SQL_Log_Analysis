import psycopg2
"""Import the psycopg  adapter to allow integration with PostgreSQL database
and the below python code"""

DBNAME = "news"


def popular_articles():
    """Returns a list most popular articles, their author, and respective
    count from newsdata.sql  """
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute("select authart.title, authart.name as author, titlecount.count \
        AS number_of_views from titlecount \
        join authart ON titlecount.title = authart.title order by count desc")
        print("Most popular articles read and their respective authors, and\
        counts:")
        print(c.fetchall())
        db.close()
    except:
        print("popular_articles function didn't run")


def popular_authors():
    """Returns a list most popular authors and the number of times their
    articles have been accessed from the newsdata.sql database."""
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute("select name, count(name) as number_of_views from logauthart group by name\
        order by number_of_views desc")
        print("List of the most popular authors accessed \
        and the respective count of articles")
        print(c.fetchall())
        db.close()
    except:
        print("popular_authors function did not run")


def days_errors():
    """Returns a list a list of all days were error rates are greater than 1%'
    and that day's percentage of errors from the newsdata.sql.  Their is
    a subquery in the execution scrip that allows for the calculation
    of the error rate from  the log. """
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute("select date, largerthan1 from (select date,(error_count\
        ::decimal/ok_count::decimal)*100 as largerthan1 from errorok) \
        as X where largerthan1 > 1")
        print("A list of all days were error rates are greater than 1%' and that day's\
        percentage of errors")
        print(c.fetchall())
        db.close()
    except:
            print("days_errors function did not run")

popular_articles()
popular_authors()
days_errors()

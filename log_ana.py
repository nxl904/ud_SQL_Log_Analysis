#!/usr/bin/env python3
import psycopg2
"""Import the psycopg  adapter to allow integration with PostgreSQL database
and the below python code"""

DBNAME = "news"


def popular_articles():
    if __name__ == '__main__':
        try:
            db = psycopg2.connect(database=DBNAME)
            c = db.cursor()
            c.execute("select authart.title, authart.name as author, titlecount.count \
            AS number_of_views from titlecount \
            join authart ON titlecount.title = authart.title order by \
            count desc")
            print("Most popular articles read(article, name, count):")
            fa = (c.fetchall())
            for n in fa:
                print(' '+str(n[0])+'by'+str(n[1])+'-'+str(n[2])+'views')
            db.close()
        except:
            print("popular_articles function didn't run")


def popular_authors():
    if __name__ == '__main__':
        try:
            db = psycopg2.connect(database=DBNAME)
            c = db.cursor()
            c.execute("select name, count(name) as number_of_views from\
                logauthart group by name order by number_of_views desc")
            print("List of the most popular authors accessed (author, count):")
            fa = (c.fetchall())
            for n in fa:
                print(' ' + str(n[0]) + ' - ' + str(n[1]) + ' views')
            db.close()
        except:
            print("popular_authors function did not run")


def days_errors():
    if __name__ == '__main__':
        try:
            db = psycopg2.connect(database=DBNAME)
            c = db.cursor()
            c.execute("select date, largerthan1 from (select date,(error_count\
            ::decimal/ok_count::decimal)*100 as largerthan1 from errorok) \
            as X where largerthan1 > 1")
            print("Dates where error rate >1% (date, percentage):")
            fa = (c.fetchall())
            for n in fa:
                print(' '+str(n[0])+" "+'date'+" "+'{:.4}'.format(str(n[1])))
            db.close()
        except:
            print("days_errors function did not run")

popular_articles()
popular_authors()
days_errors()

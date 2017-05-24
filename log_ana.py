import  psycopg2 

DBNAME = "news"


def popular_articles():
  	"""Return all posts from the 'database', most recent first."""
	try:
		db = psycopg2.connect (database =DBNAME)
		c = db.cursor()
		c.execute("select authart.title, authart.name as author, titlecount.count AS number_of_views from titlecount join authart ON titlecount.title = authart.title order by count desc")
		print("connected to db")
		print(c.fetchall()) 
		db.close()
	except:
		print("no luck")

def popular_authors():
  	"""Return all posts from the 'database', most recent first."""
	try:
		db = psycopg2.connect (database =DBNAME)
		c = db.cursor()
		c.execute("select name, count(name) as number_of_views from logauthart group by name order by number_of_views desc")
		print("connected to db")
		print(c.fetchall()) 
		db.close()
	except:
		print("no luck")

def days_errors():
  	"""Return all posts from the 'database', most recent first."""
	try:
		db = psycopg2.connect (database =DBNAME)
		c = db.cursor()
		c.execute("select date, largerthan1 from (select date,(error_count::decimal/ok_count::decimal)*100 as largerthan1 from errorok) as X where largerthan1 > 1")
		print("connected to db")
		print(c.fetchall()) 
		db.close()
	except:
		print("no luck")

popular_articles()
popular_authors()
days_errors()





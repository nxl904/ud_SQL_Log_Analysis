Description: 
This is the third project required for the Udacity Nanodegree for Full Stack Web Development. Here we are given three tables and asked to extract specific information. Demonstration of SQL topics such as joins, subqueries, view creation, char_to and sub-string parsing were used in this PostgreSQL database. I further created a simple python application and integrated it to the database using psycopg2. This applications allows for direct read integration with the backend repository enabling the user to run the queries by simply executing the python script.  All work was done in the GIT command line in a virtualized vm environment using Vagrant. 

Questions to be answered

The following three questions were proposed in this assignment given the attached newsdata.sql database:
1.	What are the most popular three articles of all time? 
2.	Who are the most popular article authors of all time? 
3.	On which days did more than 1% of requests lead to errors? 

The following three tables were also provided: 
1.	Log
2.	Articles
3.	Authors

While the articles and authors have a similar column that can be used for a join “author” in articles to “name” in authors, log does not. It’s imperative that these data points be joined if we are to answer any of these questions. There are a couple of ways that one could go about creating these queries, I decided to produce a series of logical views. There is an over use of views in this case, but it’s not without reason. In this instance I found that it was a preferable approach as it keeps the ultimate queries used in the python code more readable than a subquery would. Additionally, it allows for explanation and a demonstration of the logical flow that was necessary to obtain the answers to the questions. 

The following views were created:

authart – combines author and article tables
logsubstr – Parses the “path” column of the log file using a substring function to obtain the “slug” which will allow for a join to authart

logauthart – joins logsubstr to authart to make a single table with all necessary data points.

titlecount – queries logauthart to provide a count of titles.

time2txt- utilizes the to_char function and converts the “time” column in time2txt from a timestamp to a string.

time2txtss – utilizes the substring function to parse the “time” column form the logauthart to include only the date and not the hours, minutes, and seconds. This was necessary to aggregate and summate the log data by date to answer question 3. 

ok – view of time2txtss with only 200 responses.

error- view of time2txtss with only 404 responses.

errorok – combines counts of errors & ok to calculate error rate for question 3. 

The python code in log_ana.py was validated in accordance to PEP8 standards:  http://pep8online.com/

Install Instructions: 
1.	git clone: https://github.com/nxl904/ud_SQL_Log_Analysis.git
2.	create a local directory and unzip and save newsdata.zip and log_ana.py
3.	open up the manual_createview.text file
4.	run each one of the create view queries in the command line  of psql news to create the needed views*
5.	navigate to repository in command line and run log_ana.py

Usage: 
This python script is intended to answer the questions proposed in the Description section of this README doc. The intention is to demonstrate knowledge and practical application of the following technologies: 
-PostgreSQL
-Vagrant
-GIT
-Python – pyscopg2


* I have attached createview.py file as well. My intention was to automate the creation of the views so the user would only need to run the createview.py file first. However, I'm have issues with the execution function not firing when using "create view as."  Any feedback on how to remedy this is appreciated.


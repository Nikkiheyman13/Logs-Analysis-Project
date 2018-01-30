# Logs Analysis Project

This is the Log Analysis Project for Udacity's Full Stack Nanodegree. In this project, I've built an internal reporting tool that will use information from the database to discover what kind of articles the site's readers enjoy by using SQL queries to analyze the data and print out answers to three questions.  


## Mission

We are using the data to answer the following questions:

+ What are the most popular three articles of all time?
+ Who are the most popular article authors of all time?
+ On which days did more than 1% of requests lead to errors?

### Content

+ `news.py`: This file contains the python source code
+ `results.txt`: This is the output that is created by log_analysis.py

### Prerequisites

- [Python3](https://www.python.org/download/releases/3.0/)
- [Vagrant](https://www.vagrantup.com/)
- [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)

Clone this repository:

```
https://github.com/Nikkiheyman13/Logs-Analysis-Project.git
```

### Execute

Navigate to the project directory

Use the following code to import the data:
```
psql -d news -f newsdata.sql
```

Run the python program using the command line or terminal while in the Vagrant VM:
```
python3 news.py
```

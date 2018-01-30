#! /usr/bin/env python3
from datetime import date
import psycopg2

DB_NAME = "news"

# 1. What are the most popular three articles of all time?
query1 = """
    select articles.title, count(log.id) as views
    from log,
    articles where log.path = concat('/article/', articles.slug)
    group by articles.title
    order by views desc
    limit 3;
"""
query_1 = dict()
query_1['question'] = "\n1. The 3 most popular articles are:\n"

# 2. Who are the most popular article authors of all time?
query2 = """
    select authors.name, count(*) as num
    from authors
    join articles on authors.id = articles.author
    join log on log.path = concat ('/article/', articles.slug)
    group by authors.name
    order by num desc
    limit 3
    """

query_2 = dict()
query_2['question'] = "\n2. Top 3 authors of all time are:\n"

# 3. On which days did more than 1% of requests lead to errors?
query3 = """
    select * from (
        select date(time),
        round(
            100.0*sum(case log.status
            when '200 OK' then 0 else 1 end)/
            count(log.status),1
        ) as error
        from log
        group by date(time)
        order by error desc
    ) as subq
    where error > 1;
    """

query_3 = dict()
query_3['question'] = "\n3. Days with more than 1% of request \
that lead to an error:\n"


# returns result
def get_query_result(query):
    db = psycopg2.connect(database=DB_NAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results


# execute above queries
def print_query_results(query_result):
    print(query_result['question'])
    for result in query_result['results']:
        print('\t' + str(result[0]) + ' ---> ' + str(result[1]) + ' views')


def print_query_results_error(query_result):
    print(query_result['question'])
    for result in query_result['results']:
        print('\t' + str(result[0].strftime('%B %d, %Y')) + ' ---> ' +
               str(result[1]) + ' % errors')


# stores query result
query_1['results'] = get_query_result(query1)
query_2['results'] = get_query_result(query2)
query_3['results'] = get_query_result(query3)

# print output
print_query_results(query_1)
print_query_results(query_2)
print_query_results_error(query_3)

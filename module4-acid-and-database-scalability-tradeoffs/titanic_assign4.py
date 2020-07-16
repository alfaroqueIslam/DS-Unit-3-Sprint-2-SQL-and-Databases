import psycopg2
import sqlite3

dbname = 'qluaqybq'
user = 'qluaqybq'  # ElephantSQL chooses to reuse dbname and username
password = 'rhKOPsVgTV7sCwsgto06CoCc7ES-GCUz'
host = 'ruby.db.elephantsql.com'  # Port is default 5432

pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)

pg_curs = pg_conn.cursor()

#How many passengers survived, and how many died?

#How many passengers were in each class?
#How many passengers survived/died within each class?
#What was the average age of survivors vs nonsurvivors?
#What was the average age of each passenger class?
#What was the average fare by passenger class? By survival?
#How many siblings/spouses aboard on average, by passenger class? By survival?
#How many parents/children aboard on average, by passenger class? By survival?
#Do any passengers have the same name?

#!/usr/bin/env python
import psycopg2
import sqlite3
import pandas as pd 

df = pd.read_csv("titanic.csv")

conn = sqlite3.connect("titanic.sqlite3")
curs = conn.cursor()
df.to_sql('titanic', con=conn)
print(curs.execute("SELECT COUNT(*) FROM titanic;").fetchall())

dbname = 'qluaqybq'
user = 'qluaqybq'  # ElephantSQL chooses to reuse dbname and username
password = 'rhKOPsVgTV7sCwsgto06CoCc7ES-GCUz'
host = 'ruby.db.elephantsql.com'  # Port is default 5432

pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)

pg_curs = pg_conn.cursor()

sl_conn = sqlite3.connect('titanic.sqlite3')
sl_curs = sl_conn.cursor()
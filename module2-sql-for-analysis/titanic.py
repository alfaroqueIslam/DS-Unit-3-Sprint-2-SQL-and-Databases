#!/usr/bin/env python
import psycopg2
import sqlite3
import pandas as pd 

df = pd.read_csv("titanic.csv")

conn = sqlite3.connect("titanic.sqlite3")
curs = conn.cursor()
#df.to_sql('titanic', con=conn)
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

pg_curs.execute("""DROP TABLE IF EXISTS titanic;""")
pg_conn.commit()

create_titanic_table = """
CREATE TABLE titanic (
  index SERIAL PRIMARY KEY,
  Survived INT,
  Pclass INT,
  Name TEXT,
  Sex TEXT,
  Age REAL,
  Siblings_Spouses_Aboard INT,
  Parents_Children_Aboard INT,
  Fare REAL
);
"""

pg_curs = pg_conn.cursor()
pg_curs.execute(create_titanic_table)
pg_conn.commit()

sl_curs.execute(""" UPDATE titanic
SET Name = REPLACE(Name, "'", ' '); """)

get_person = 'SELECT * FROM titanic;'
people = sl_curs.execute(get_person).fetchall()


for person in people:
    insert_person = """
    INSERT INTO titanic
    (Survived,Pclass,Name,Sex,Age,Siblings_Spouses_Aboard,Parents_Children_Aboard,fare)
    VALUES """ + str(person[1:]) + ";"
    pg_curs.execute(insert_person)

pg_conn.commit()
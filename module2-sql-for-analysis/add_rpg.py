#!/usr/bin/env python
import psycopg2
import sqlite3

dbname = 'qluaqybq'
user = 'qluaqybq'  # ElephantSQL chooses to reuse dbname and username
password = 'rhKOPsVgTV7sCwsgto06CoCc7ES-GCUz'
host = 'ruby.db.elephantsql.com'  # Port is default 5432

pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)

pg_curs = pg_conn.cursor()

sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

get_characters = 'SELECT COUNT(*) FROM charactercreator_character;'
characters = sl_curs.execute(get_characters).fetchall()


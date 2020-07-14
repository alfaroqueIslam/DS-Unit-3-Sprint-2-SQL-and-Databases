#!/usr/bin/env python

import sqlite3
import pandas as pd 

df = pd.read_csv("titanic.csv")

conn = sqlite3.connect("titanic.sqlite3")
curs = conn.cursor()
df.to_sql('titanic', con=conn)
print(curs.execute("SELECT COUNT(*) FROM titanic;").fetchall())
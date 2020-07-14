#!/usr/bin/env python

import sqlite3
import pandas as pd 

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/00476/buddymove_holidayiq.csv")

conn = sqlite3.connect("buddymove_holidayiq.sqlite3")
curs = conn.cursor()
#df.to_sql('buddymove_holidayiq', con=conn)
print(curs.execute("SELECT COUNT(*) FROM buddymove_holidayiq").fetchall())
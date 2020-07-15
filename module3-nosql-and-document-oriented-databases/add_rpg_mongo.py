#!/usr/bin/env python

import pymongo
import sqlite3


sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

get_characters = 'SELECT * FROM charactercreator_character;'
characters = sl_curs.execute(get_characters).fetchall()

client = pymongo.MongoClient("mongodb+srv://alfaroque5:dAsF9ZRMS1gM2Wah@cluster0.jij4e.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = client.test

character_docs = []
for character in characters:
  doc = {'character_id' : character[0],
  'name' : character[1],
  'level' : character[2],
  'exp' : character[3],
  'hp' : character[4],
  'strength' : character[5],
  'intelligence' : character[6],
  'dexterity' : character[7],
  'wisdom' : character[8]}
  character_docs.append(doc)

db.test.insert_many(character_docs)





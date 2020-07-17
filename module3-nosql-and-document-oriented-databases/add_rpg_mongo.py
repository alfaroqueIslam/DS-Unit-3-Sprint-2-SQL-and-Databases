#!/usr/bin/env python

import pymongo
import sqlite3


sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

get_characters = 'SELECT * FROM charactercreator_character;'
characters = sl_curs.execute(get_characters).fetchall()

get_inventory = 'SELECT * FROM charactercreator_character_inventory;'
inventory = sl_curs.execute(get_inventory).fetchall()

get_items = 'SELECT * FROM armory_item;'
items = sl_curs.execute(get_items).fetchall()

get_weapons = 'SELECT * FROM armory_weapon;'
weapons = sl_curs.execute(get_weapons).fetchall()

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

inventory_docs = []
for invent in inventory:
  doc = {'id' : inventory[0], 
  'character_id' : inventory[1],
  'item_id' : inventory[2]}
  
  inventory_docs.append(doc)

item_docs = []
for item in items:
  doc = {'item_id' : item[0]}

  item_docs.append(doc)

weapon_docs = []
for weapon in weapons:
  doc = {'item_ptr_id' : weapon[0]}

  weapon_docs.append(doc)

db.test.insert_many(character_docs)





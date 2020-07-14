#!/usr/bin/env python
"""
Our Questions:
    How many total Characters are there?
    How many of each specific subclass?
    How many total Items?
    How many of the Items are weapons? How many are not?
    How many Items does each character have? (Return first 20 rows)
    How many Weapons does each character have? (Return first 20 rows)
    On average, how many Items does each Character have?
    On average, how many Weapons does each character have?
"""
import sqlite3
conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()
# How many total Characters? Table: charactercreator_character
count_characters = 'SELECT COUNT(*) FROM charactercreator_character;'
print(curs.execute(count_characters).fetchall())

# How many total Clerics? Table: charactercreator_cleric
count_cleric = 'SELECT COUNT(*) FROM charactercreator_cleric;'
print(curs.execute(count_cleric).fetchall())

# How many total Fighters? Table: charactercreator_fighter
count_fighter = 'SELECT COUNT(*) FROM charactercreator_fighter;'
print(curs.execute(count_fighter).fetchall())

# How many total Mages? Table: charactercreator_mage
count_mage = 'SELECT COUNT(*) FROM charactercreator_mage;'
print(curs.execute(count_mage).fetchall())

# How many total Theifs? Table: charactercreator_thief
count_thief = 'SELECT COUNT(*) FROM charactercreator_thief;'
print(curs.execute(count_thief).fetchall())

# How many total Necromancers? Table: charactercreator_necromancer
count_necromancer = 'SELECT COUNT(*) FROM charactercreator_necromancer;'
print(curs.execute(count_necromancer).fetchall())

# How many total items? Table: armory_item
count_items = 'SELECT COUNT(*) FROM armory_item;'
print(curs.execute(count_items).fetchall())

# How many total weapons? Table: armory_weapon
count_weapon = 'SELECT COUNT(*) FROM armory_weapon;'
print(curs.execute(count_weapon).fetchall())

# How many total items that are not weapons? Table: armory_item
'''count_notweapon = 'SELECT COUNT(*) FROM armory_item MINUS SELECT COUNT(*) FROM armory_weapon;'
print(curs.execute(count_notweapon).fetchall())'''

# How many Items does each character have? (Return first 20 rows)
count_distinct = 'SELECT COUNT(DISTINCT character_id) FROM charactercreator_character_inventory;'
print(curs.execute(count_distinct).fetchall())
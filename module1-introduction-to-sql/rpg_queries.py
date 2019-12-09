import sqlite3

conn = sqlite3.connect('rpg_db')
curs = conn.cursor()

# How many total characters are there?
# curs.execute(query1).fetchone()
query1 = 'SELECT COUNT(name) FROM charactercreator_character'
print('Total number of Characters:', curs.execute(query1).fetchone())

# How many of each specific subclass?
query2a = 'SELECT COUNT(character_ptr_id) FROM charactercreator_fighter'
print('Total number of fighters:', curs.execute(query2a).fetchone())

query2b = 'SELECT COUNT(character_ptr_id) FROM charactercreator_cleric'
print('Total number of clerics:', curs.execute(query2b).fetchone())

query2c = 'SELECT COUNT(character_ptr_id) FROM charactercreator_mage'
print('Total number of mages:', curs.execute(query2c).fetchone())

query2d = 'SELECT COUNT(character_ptr_id) FROM charactercreator_theif'
print('Total number of thiefs:', curs.execute(query2d).fetchone())

# How many total items?
query3 = 'SELECT COUNT(name) FROM armory_item'
print('Total number of items:', curs.execute(query3).fetchone())

# How many of the items are weapons?
query4 = 'SELECT COUNT(item_ptr_id) FROM armory_weapons'
print('Total number of weaponary items:', curs.execute(query4).fetchone())


# How many are not weapons?
# How many Items does each character have? (Return first 20 rows)
# How many Weapons does each character have? (Return first 20 rows)
# On average, how many Items does each Character have?
# On average, how many Weapons does each character have?

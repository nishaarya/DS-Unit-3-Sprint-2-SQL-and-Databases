import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

# How many total characters are there?
# curs.execute(query1).fetchone()
query1 = 'SELECT COUNT(*) FROM charactercreator_character'
print('Total number of Characters:', curs.execute(query1).fetchone())

# How many of each specific subclass?
query2a = 'SELECT COUNT(*) FROM charactercreator_fighter'
print('Total number of fighters:', curs.execute(query2a).fetchone())

query2b = 'SELECT COUNT(*) FROM charactercreator_cleric'
print('Total number of clerics:', curs.execute(query2b).fetchone())

query2c = 'SELECT COUNT(*) FROM charactercreator_mage'
print('Total number of mages:', curs.execute(query2c).fetchone())

query2d = 'SELECT COUNT(*) FROM charactercreator_thief'
print('Total number of thiefs:', curs.execute(query2d).fetchone())

# How many total items?
query3 = 'SELECT COUNT(*) FROM armory_item'
print('Total number of items:', curs.execute(query3).fetchone())

# How many of the items are weapons?
query4 = 'SELECT COUNT(*) FROM armory_weapon'
print('Total number of weaponary items:', curs.execute(query4).fetchone())

# How many Items does each character have (first 20 rows):
query5 = """
SELECT COUNT(CCI.item_id)
FROM charactercreator_character as CC,
charactercreator_character_inventory as CCI
WHERE CCI.character_id = CC.character_id
GROUP BY CC.character_id;
"""
print('Number of items per character:', curs.execute(query5).fetchmany(20))

# How many weapons does each character have (first 20 rows):
query6 = """
SELECT COUNT(AW.item_ptr_id)
FROM charactercreator_character_inventory as CCI,
charactercreator_character as CC,
armory_item as AI,
armory_weapon as AW
WHERE CCI.character_id = CC.character_id
AND CCI.item_id = AI.item_id
AND AI.item_id = AW.item_ptr_id
GROUP BY CC.character_id;
"""
print('Number of weapons per character:', curs.execute(query6).fetchmany(20))

# On average, how many Items does each character have:
query7 = """
SELECT AVG(avg_items)
FROM(SELECT COUNT(CCI.item_id) as avg_items
FROM charactercreator_character as CC,
charactercreator_character_inventory as CCI
WHERE CCI.character_id = CC.character_id
GROUP BY CC.character_id) AS T;
"""
print('Average num of items per character:', curs.execute(query7).fetchone())

# On average, how many Weapons does each character have:
query8 = """
SELECT AVG(avg_weaps)
FROM (SELECT COUNT(AW.item_ptr_id) as avg_weaps
FROM charactercreator_character_inventory as CCI,
charactercreator_character as CC,
armory_item as AI,
armory_weapon as AW
WHERE CCI.character_id = CC.character_id
AND CCI.item_id = AI.item_id
AND AI.item_id = AW.item_ptr_id
GROUP BY CC.character_id) AS Z;
"""
print('Average num of weapons per character:', curs.execute(query8).fetchone())

curs.close()
conn.commit()

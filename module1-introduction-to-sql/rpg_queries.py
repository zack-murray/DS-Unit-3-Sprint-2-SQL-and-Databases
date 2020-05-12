import os 
import sqlite3

DB_FILEPATH = os.path.join(os.path.dirname(__file__),"rpg_db.sqlite3")
conn = sqlite3.connect(DB_FILEPATH)
# conn.row_factory = sqlite3.Row
curs = conn.cursor()

# How many total Characters are there?
tot_char_query = '''
SELECT
    *
FROM charactercreator_character
'''
total_chars =  curs.execute(tot_char_query).fetchall()
print("Total # of characters", len(total_chars))

# How many of each specific subclass?
cleric_query = 'SELECT * FROM charactercreator_cleric'
fighter_query = 'SELECT * FROM charactercreator_fighter'
mage_query = 'SELECT * FROM charactercreator_mage'
necromancer_query = 'SELECT * FROM charactercreator_necromancer'
thief_query = 'SELECT * FROM charactercreator_thief'
cleric_subclass = curs.execute(cleric_query).fetchall()
fighter_subclass = curs.execute(fighter_query).fetchall()
mage_subclass = curs.execute(mage_query).fetchall()
necromancer_subclass = curs.execute(necromancer_query).fetchall()
thief_subclass = curs.execute(thief_query).fetchall()
print("Total # of clerics", len(cleric_subclass))
print("Total # of fighters", len(fighter_subclass))
print("Total # of mages", len(mage_subclass))
print("Total # of necromancers", len(necromancer_subclass))
print("Total # of thieves", len(thief_subclass))

# How many total items?
tot_item_query = '''
SELECT
    *
FROM armory_item
'''

total_items = curs.execute(tot_item_query).fetchall()
print("Total # of items", len(total_items))

# How many of the items are weapons? How many are not?
tot_weapon_query = '''
SELECT
    *
FROM armory_weapon
'''
total_weapons = curs.execute(tot_weapon_query).fetchall()
print("Total # of weapons", len(total_weapons))
print("Total # of non-weapons",(len(total_items) - len(total_weapons)))

# How many items does each character have? (Return first 20 rows)
items_per_query = '''
SELECT
    character_id as CharacterId
    ,count(item_id) as NumItems
FROM charactercreator_character_inventory
GROUP BY character_id
LIMIT 20
'''
items_per =  curs.execute(items_per_query).fetchall()
print("Total # of items per character", items_per)

# How many weapons does each character have? (Return first 20 rows) 
weaps_per_query = '''
SELECT
	character_id as CharacterId
	,count(aw.item_ptr_id) as NumWeapons
FROM charactercreator_character_inventory as cci
LEFT JOIN armory_weapon as aw on cci.item_id = aw.item_ptr_id
GROUP BY character_id
LIMIT 20
'''
weaps_per = curs.execute(weaps_per_query).fetchall()
print("Total # of weapons per character", weaps_per)

# On average, how many items does each character have?
ave_item_query = '''
SELECT
	avg(NumItems) as AverageNumItems
FROM (
	SELECT
    	character_id as CharacterId
    	,count(item_id) as NumItems
	FROM charactercreator_character_inventory
	GROUP BY character_id
)
'''
ave_items = curs.execute(ave_item_query).fetchall()
print("Average # of items per character", ave_items)

# On average, how many weapons does each character have?
ave_weap_query = '''
SELECT
	avg(NumWeapons) as AverageNumWeapons
FROM (
    SELECT
        character_id as CharacterId
        ,count(aw.item_ptr_id) as NumWeapons
    FROM charactercreator_character_inventory as cci
    LEFT JOIN armory_weapon as aw on cci.item_id = aw.item_ptr_id
    GROUP BY character_id
)
'''
ave_weaps = curs.execute(ave_weap_query).fetchall()
print("Average # of items per character", ave_weaps)

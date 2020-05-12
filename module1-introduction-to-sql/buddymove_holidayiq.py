import pandas as pd
import sqlite3

df = pd.read_csv('buddymove_holidayiq.csv')
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
df.to_sql("buddymove", con=conn)

# How many rows do we have? (should be 249)
row_query = '''
SELECT
    count('User Id') as NumUsers
FROM buddymove
'''
total_rows =  conn.execute(row_query).fetchone()
print("Total # of rows", total_rows)

# How many users reviewed at least 100 nature and 100 shopping?

review_query = '''
SELECT
	count('User Id')
FROM buddymove
WHERE Nature >= 100 and Shopping >= 100
'''
review_users = conn.execute(review_query).fetchone()
print("Amount of users who reviewed 100 nature and shopping category", review_users)

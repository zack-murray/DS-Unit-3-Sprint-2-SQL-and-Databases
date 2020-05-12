  
import os
from sqlalchemy import create_engine
import sqlite3
from dotenv import load_dotenv
import pandas as pd

# instantiate titanic data
df = pd.read_csv('titanic.csv')

# Change the columns to be more sql friendly
df.columns = ['survived', 'pclass', 'name', 'sex', 'age',
'siblings_spouses_aboard', 'parents_children_aboard', 'fare']
print(df.columns)

# Set up .env variables to connect to postgres later
envpath = os.path.join(os.getcwd(), '.env')

# print(envpath)
load_dotenv()

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')

# Set connection to PostgreSQL
sql_url = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}'
engine = create_engine(sql_url)

# Copy df to new table in PostgreSQL
df.to_sql('titanic_data', engine, if_exists='replace')

# Query to find # of passengers survived(=1)/died(=0)
print('Survival Rate')

survive_query = '''
SELECT
    survived as LifeStatus
    ,count(survived) as SurvivalCount
FROM titanic_data
GROUP BY survived
'''

print(pd.read_sql(survive_query, engine))

# Query to find # of passengers among pclasses (1=1st/2=2nd/3=3rd)
print('Class Warfare')

class_query = '''
SELECT
    pclass as PassengerClass
    ,count(pclass) as ClassCount
FROM titanic_data
GROUP BY pclass
ORDER BY pclass ASC
'''

print(pd.read_sql(class_query, engine))

# Query to find # of men vs women 
print('Sex Differential')

sex_query = '''
SELECT
    sex as Gender
    ,count(sex) as SexCount
FROM titanic_data
GROUP BY sex
'''

print(pd.read_sql(sex_query, engine))

# Query to find the average fare aboard
print('Average Fare')

fare_query = '''
SELECT
    AVG(fare)
FROM titanic_data
'''

print(pd.read_sql(fare_query, engine))
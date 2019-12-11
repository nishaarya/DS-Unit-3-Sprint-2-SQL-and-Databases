import pandas as pd
import numpy as np
import sqlite3

# Read in CSV file.
df = pd.read_csv('buddymove_holidayiq.csv')

# Get rid of space in column names.
df.columns = df.columns.str.replace(' ', '_')

# Check shape and null values to verify correctly imported dataframe.
print(df.shape)
print(df.isnull().sum())

# Make connection and create new database file.
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = conn.cursor()

df.to_sql('review', con=conn)

# How many rows are there?
query1 = 'SELECT COUNT(*) FROM review';
print('Number of rows are:', curs.execute(query1).fetchone())

# How many users who reviewed at least 100 Nature in the category also reviewed
# at least 100 in the Shopping category?
query2 = 'SELECT COUNT(*) FROM review WHERE Nature >=100 AND Shopping >=100';
print('Users who reviewed at least 100 in both Nature and Shopping:',
      curs.execute(query2).fetchone())

curs.close()
conn.commit()

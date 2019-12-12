import pandas as pd
import numpy as np
import psycopg2 as pg2
import sqlite3

# First we need to read in CSV file:
df = pd.read_csv('titanic.csv')

# Then we do some Data Wrangling
df.columns = df.columns.str.replace(' ', '_')
df.columns = df.columns.str.replace('/', '_')
df.Name = df.Name.str.replace("'", " ")

# This is to find the longest name to help us with the table creation
df.Name.map(lambda x: len(x)).max()

# Check shape and null values to verify correctly imported dataframe.
print(df.shape)
print(df.isnull().sum())

# Sqlite3 connection
sq_conn = sqlite3.connect('titanic.sqlite3')

# Sqlite3 cursor
sq_curs = sq_conn.cursor()

# Change csv file to sql
df.to_sql('df', conn, if_exists = 'replace')

# Database information from elephantSQL:
dbname = 'dbname from elephantSQL'
user = 'user from elephantSQL'
password = 'password from elephantSQL'
host = 'host from elephantSQL'

# make a connection
conn = psycopg2.connect(dbname = 'rdwxinbk',
                        user = 'rdwxinbk',
                        password = 'nPlt4RsZDjw9OvjoSGWL5MdpO8pF-FOV',
                        host = 'manny.db.elephantsql.com')

# make a cursor
curs = conn.cursor()

# Drop the below because I've ran it before
# sq_curs.execute('DROP TABLE titanic_sql;')

# Turn CSV into sqlite3 table so can turn into postgres table:
df.to_sql('titanic_sql', con=sq_conn)

# Save it to a variable
passengers = sq_curs.execute('SELECT * from titanic_sql;').fetchall()

# Drop the table if you run it again
# curs.execute('DROP TABLE insert_titanic')

# Create insert_titanic table:
create_insert_titanic = """
CREATE TABLE insert_titanic (
Passenger_ID SERIAL PRIMARY KEY,
Survived INT,
Pclass INT,
Name VARCHAR(85),
Sex VARCHAR(85),
Age FLOAT,
Siblings_Spouses_Aboard INT,
Parents_Children_Aboard INT,
Fare FLOAT
);
"""
# Execute:
pg_curs.execute(create_insert_titanic)


# For loop to insert all data from sqlite3 table into postgres table:
for passenger in passengers:
    insert_passenger = """
        INSERT INTO insert_titanic
        (Survived, Pclass, Name, Sex, Age, Siblings_Spouses_Aboard,
        Parents_Children_Aboard, Fare)
        VALUES """ + str(passenger[1:]) + ";"
    curs.execute(insert_passenger)

curs.execute('SELECT * from insert_titanic;')
curs.fetchall()

# Close connections and commit changes:
curs.close()
conn.commit()
sq_curs.close()
sq_conn.commit()

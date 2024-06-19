import os
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()

def connect():
    global engine
    connection_string = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}?autocommit=true"
    print("Starting the connection...")
    engine = create_engine(connection_string)
    engine.connect()
    return engine

# 1) Connect to the database here using the SQLAlchemy's create_engine function
engine = connect()
# 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function
with open('src/sql/create.sql', 'r') as file:
    create_sql = file.read()
    engine.execute(create_sql)
# 3) Execute the SQL sentences to insert your data using the SQLAlchemy's execute function
with open('src/sql/insert.sql', 'r') as file:
    insert_sql = file.read()
    engine.execute(insert_sql)
# 4) Use pandas to print one of the tables as dataframes using read_sql function
df = pd.read_sql('SELECT * FROM your_table_name', engine)
print(df)
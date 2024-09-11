import os
import psycopg2
import numpy as np
import pandas  as pd
from dotenv import load_dotenv

load_dotenv()

hostname = os.getenv("hostname")
database = os.getenv("database")
username = os.getenv("username")
password = os.getenv("pwd")
port_id =os.getenv("port_id")
conn  = None
cur = None


# Defining function to connect postgres database 
def connect_db(hostname,database,username,password,port_id,conn=None,cur=None):
    try:
        conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = password,
        port = port_id)
        
        cur = conn.cursor()

        script = 'select * from sentiments'

    
        cur.execute(script)
        data = cur.fetchall()

        return data

    except Exception as e:
        print(e)

    finally:
        if conn is not None:
            conn.close()
        if cur is not None:
            cur.close()


# calling connect db function
data = connect_db(hostname,database,username,password,port_id)

# Convering Data into Dataframe using pandas

dataframe = pd.DataFrame(data=data,columns=['Review','Category'])
print(dataframe.head())

# Save file on artifacts folder
folder_path = 'D:/projects/sentiments_analysis/artifacts'

# create a folder if doesn't exists
os.makedirs(folder_path,exist_ok=True)

# define file name
file_name = 'raw_data.csv'

# creating full file path
file_path = os.path.join(folder_path,file_name)

# save file 
dataframe.to_csv(file_path,index=False)





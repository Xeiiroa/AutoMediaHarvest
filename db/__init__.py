from os import path
import os
import sqlite3
import sqlalchemy





DB_NAME = 'mediaids.db' 

def create_database():
    global con
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()
    try:
        cur.execute('CREATE TABLE mediaids(ids)')
    except sqlite3.OperationalError:
        pass
    
    


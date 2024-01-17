import logging
import sqlite3
from . import DB_NAME

class Data:
    def __init__(self):
        self.DB_NAME = str(DB_NAME)
        self.con = sqlite3.connect(DB_NAME)
        self.cur = self.con.cursor()
    
    def add_id(self, Id:str):
        try: 
            self.cur.execute('INSERT INTO mediaids VALUES(?, ?)',(None, Id))
            self.con.commit()
            return 200
        except Exception as e:
            logging.error(f'A SQL error has occured when trying to add media Id to table: {str(e)}')
            self.con.rollback()
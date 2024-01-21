import logging
import sqlite3
from . import DB_NAME
from tools.error_report import write_error

class Data:
    def __init__(self):
        self.DB_NAME = str(DB_NAME)
        self.con = sqlite3.connect(DB_NAME)
        self.cur = self.con.cursor()
    
    def add_id(self, Id:str):
        try: 
            self.cur.execute('INSERT INTO mediaids VALUES(?)',(Id,))
            self.con.commit()
            return 200
        except Exception as e:
            error_message = f'A SQL error has occured when trying to add media Id to table: {str(e)}'
            logging.error(error_message)
            write_error(error_message)
            self.con.rollback()
            
    def check_id_exists(self, Id:str):
        try:
            res = self.cur.execute('SELECT mediaid FROM mediaids WHERE mediaid = ?', (Id,))
            if res.fetchone() is None:
                return False
            else:
                return True
        except Exception as e:
            error_message = f'A SQL error has occured when trying search for id from table: {str(e)}'
            logging.error(error_message)
            
    def list_all_ids(self):
        try:
            self.cur.execute('SELECT mediaid FROM mediaids')
            values = self.cur.fetchall()
            id_list = [value[0] for value in values]
            return id_list
            
        except Exception as e:
            error_message = f'A SQL error has occured when list all ids from table: {str(e)}'
            logging.error(error_message)
            
            
    
        
         
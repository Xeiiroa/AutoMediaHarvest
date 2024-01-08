import logging

from sqlalchemy import select, Text, update, MetaData, Table, create_engine, insert
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from . import engine
from .id_table import MediaIdTable


class Data:
    def add_id(self, newId): #checks for duplicate ids and if no match is found adds newId to mediaId column in table
        with Session(engine) as session:
            try:
                if not session.query(MediaIdTable).filter_by(mediaId=newId):
                    session.execute(insert(MediaIdTable).values(mediaId=newId))
                    session.commit()  
            except SQLAlchemyError as e:
                logging.error(f'A SQL error has occured when trying to add media Id to table: {str(e)}')
                session.rollback()
        
    
    def clear_ids(self): #using an update statment clears all existing ids from database
        with Session(engine) as session:
            try:
                clear = None
                
                session.execute(update(MediaIdTable).values(mediaId=clear))
                session.commit()
            except SQLAlchemyError as e:
                logging.error(f'A SQL error has occured when trying to clear ids in table: {str(e)}')
                session.rollback()
                
    def list_ids(self):
       with Session(engine) as session:
            try:
                
                ids = []
                for media_id in session.query(MediaIdTable.mediaId).distinct():
                    ids.append(media_id)
                
                return ids
            
            except SQLAlchemyError as e:
                logging.error(f'A SQL error has occured when trying list ids from table: {str(e)}')
                return None
            
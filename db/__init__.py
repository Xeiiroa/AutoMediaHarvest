from os import path
import os

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from .id_table import MediaIdTable, Base



DB_NAME = 'mediaIds.db' 
engine = create_engine(f'sqlite:///{DB_NAME}', echo=True)

def create_database():
    if not path.exists('db/' + DB_NAME):
        global engine
        engine = create_engine(f'sqlite:///{DB_NAME}', echo=True)
        
        Base.metadata.create_all(engine)
        
        with Session(engine) as session:
            default_settings = MediaIdTable()
            session.add(default_settings)
            session.commit()
import re
import logging

from sqlalchemy import select, Text, update, MetaData, Table, create_engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv
import tkinter as tk
from tkinter import filedialog

from . import engine
from .models import Settings

class data:
    def __init__(self):
        pass
    
    def get_video_save_path(self):
        with Session(engine) as session:
            try:
                settings_row = session.scalar(select(Settings))
                print(settings_row.video_save_path)
                return settings_row.video_save_path
            except SQLAlchemyError as e:
                logging.error(f"An SQL error has occured when trying to get video save path: {str(e)}")
                
    def change_video_save_path(self):
        with Session(engine) as session:
            try:
                new_savepath = filedialog.askdirectory(title="Select a folder")
                print(f"savepath updated to {new_savepath}")
                new_savepath == None
                if new_savepath == None:
                    return
                session.execute(update(Settings).values(video_save_path=new_savepath))
                session.commit()
            except SQLAlchemyError as e:
                logging.error(f"An SQL error has occured when trying to change video save path: {str(e)}")
                session.rollback()
                
                
    def get_album_name(self):
        with Session(engine) as session:
            try:
                settings_row = session.scalar(select(Settings))
                return settings_row.album_name
            except SQLAlchemyError as e:
                logging.error(f"An SQL error has occured when trying to retrieve the album name")
                
                
                
    def change_album_name(self, new_album_name):
        with Session(engine) as session:
            try:
                session.execute(update(Settings).values(delay_time=new_album_name))
                session.commit()
                return
            except (SQLAlchemyError, ValueError) as e:
                logging.error(f"An error has occured when attempting to change delay time: {str(e)}")
                session.rollback()
        
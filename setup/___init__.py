import time
import os
import schedule
import sys
import logging
from datetime import datetime, timedelta

"""
Tasks to run and there time signatures

Download videos to pc - every 1-2 days at 12pm or set it to specific days of the week, for days i train or days off
    search albums
    use download function
    add media ids of downloaded content to database
    
clear media from album/account every 3 days at 11:59pm

###ERROR HANDLING###

in the case that the script stopps working i want an error popup screen to occur that prints the error that stopeed the program from running

"""


class AutoMediaHarvest:
    def __init__(self):
        schedule.every().day.at('4:00').do(self.Download_videos)
        schedule.every().day.at('9:00').do(self.clear_media_ids)
        
        
         
    def Download_videos(self, Mediaid):
        target_days = [1, 3, 6]
        current_day = datetime.now().weekday()
        if current_day in target_days:
            try:
                from utils.albums import AlbumRouter as albums
                from utils.downloads import Downloads as downloads
                
                Albums = albums()
                albumId = self.Albums.search_album()
                if albumId == None:
                    albumId = self.Albums.create_album()
                    return #no point in progressing in the function if the album was made today
                else:
                    Downloads = downloads()
                    self.save_media(albumId)
                     
            except Exception as e:
                logging.error(f'An error has occured when trying to run Media downloads on schedule: {str(e)}')
                self.stop_app()
        else:
            return
        
        
        
    def clear_media_ids(self):
        target_days = [1, 3, 6]
        current_day = datetime.now().weekday()
        if current_day in target_days:
            try:
                from utils.albums import AlbumRouter as albums
                from db.data_functions import Data as data
                
                Albums = albums()
                albumId = self.Albums.search_album()
                if albumId == None:
                    raise Exception('Album not found to be cleared under scheduled task')
                else:
                    self.Albums.clear_album(albumId)
                    Data = data()
                    self.Data.clear_ids()
                    
            except Exception as e:
                logging.error(f'An error has occured when trying to run Media downloads on schedule: {str(e)}')
                self.stop_app()
                
        
        """
        call remove media function from album and from account
        clear ids from database
        """
        
        
    def stop_app(self):
        schedule.clear()
        sys.exit()
        
        
    
        
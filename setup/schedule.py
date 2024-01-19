import time
import os
import schedule
import sys
import logging
from datetime import datetime, timedelta
from tools.error_report import write_error

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
                    self.save_album_media(albumId)
                     
            except Exception as e:
                error_message = f'An error has occured when trying to run Media downloads on schedule: {str(e)}'
                logging.error(error_message)
                self.stop_app(error_message)
        else:
            return
        
        
    #* if there is no way of deleting videos from google photos account theres not really a need to have a remove from album function as im just gonna delete them manually
    def clear_media_ids(self): 
        target_days = [1, 3, 6]
        current_day = datetime.now().weekday()
        if current_day in target_days:
            try:
                from utils.albums import AlbumRouter as albums
                from db.data_functions import Data as Db
                
                Albums = albums()
                albumId = self.Albums.search_album()
                if albumId == None:
                    raise Exception('Album not found to be cleared under scheduled task')
                else:
                    self.Albums.clear_album(albumId)
                    #!check backlog to see if a clear id function is needed
                    #Data = Db() #? not sure if the call of the data module needs to be a self argument
                    #Data.clear_ids() #? ^^^
                    
            except Exception as e:
                error_message=f'An error has occured when trying to run Media downloads on schedule: {str(e)}'
                logging.error(error_message)
                self.stop_app()
            
        
        
    def stop_app(self):
        schedule.clear()
        sys.exit()
        
        
    
        
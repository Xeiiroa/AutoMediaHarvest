import time
import os
import sys
import logging
from datetime import datetime, timedelta
from tools.error_report import write_error
#from utils.albums import AlbumRouter as Album #! may not be needed as they are called in function where they are needed 
#from utils.downloads import Downloads as Download #!^^^
from db.data_functions import Data as Db


class AutoMediaHarvest:
    def __init__(self):
        #! NOTE WHEN CHANGING FUNCTIONS: try to make sure these 2 functions run on different days, preferrably have clear media ids run 2-3 days from last occurence of 
        self.download_videos()
        self.clear_media_ids()
        
    
    def download_videos(self):
        target_days = [0,1,3,5] #0-6,(where Monday is 0 and Sunday is 6)
        current_day = datetime.now().weekday()
        if current_day in target_days:
            try:
                from utils.albums import AlbumRouter as Album
                from utils.downloads import Downloads as Download
                
                Albums = Album()
                albumId = Albums.search_album() 
                if albumId == None:
                    albumId = Albums.create_album()
                    album_default_image_id = Albums.create_image()
                    Albums.import_image(albumId, album_default_image_id)
                    return #no point in progressing in the function if the album was made in this instance 
                else:
                    Downloads = Download()
                    Downloads.save_album_media(albumId)
                     
            except Exception as e:
                error_message = f'An error has occured when trying to run Media downloads with windows task scheduler: {str(e)}'
                logging.error(error_message)
                write_error(error_message)
                self.stop_app()
        else:
            return
        
    
    def clear_media_ids(self):
        target_days = [6] #only runs on Sunday at the moment, if google photos storage becomes an issue, add 4 to the list for it to also delete on thursdays
        current_day = datetime.now().weekday()
        if current_day in target_days:
            try:
                from utils.albums import AlbumRouter as Album
                from db.data_functions import Data as Db
                
                Albums = Album()
                albumId = Albums.search_album()
                if albumId == None:
                    raise Exception('Album was not found therefore it is unable to be cleared')
                else:
                    Albums.clear_album(albumId)
                    #!check backlog to see if a clear id function is needed, if so read the calls below
                    #Data = Db()
                    #Data.clear_ids()
                    
            except Exception as e:
                error_message=f'An error has occured when trying to clear ids with windows task scheduler: {str(e)}'
                logging.error(error_message)
                write_error(error_message)
                self.stop_app()
    
    def stop_app(self):
        sys.exit()
        
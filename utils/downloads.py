#todo create a class that may have to user albums as an inheritence 
# this class will have all functions related to downloading videos from an album

import os
from tools.service import prompt_permission
import requests #type: ignore
import pandas as pd
from db.data_functions import Data as Db
from config import Settings as Config
import logging
from tools.error_report import write_error



class Downloads(): #check that everything that imports classes has the import statement with 'Downloads' capitalizsed
    def __init__(self):
        Config = Config()
        self.savepath = Config.get_setting('videoSavepath')
        self.service = prompt_permission() #may not be needed since it inherits from album router
        
        
        
    
    def process_file(self, url:str, destination_folder:str, file_name:str): 
        #* url acts as the place were content is grabbed (in case i forget)
        response = requests.get(url)
        if response.status_code == 200:
            print('Downloading file {0}'.format(file_name))
            with open(os.path.join(destination_folder, file_name), 'wb') as f:
                f.write(response.content)
                f.close()
    
        
    def save_album_media(self, album_id:str): #add id save function to this
        """
        ___Possible errors to keep track of in this current version of this function___ 1/18/24
        
        - There is a chance that an album that has duplicates of the same item wont print an id for that item which can break the iterations of my current for loop
        - But since its just for me i can follow the honor system
        """
        Data=Db()
        media_files = self.service.mediaItems().search(body={'albumId': album_id}).execute()['mediaItems']
        already_SavedMediaIds = Data.list_all_ids()
        album_media_ids = [item['id'] for item in media_files]
        
        for iteration, media_file in enumerate(media_files):
            file_name=media_file['filename']
            download_url = media_file['baseUrl'] + '=d'
            mediafile_id = album_media_ids[iteration] #could use iter but this is what i know 
            if mediafile_id in already_SavedMediaIds:
                continue
            
            try:
                Data.add_id(album_media_ids[iteration])
                self.process_file(download_url, self.savepath, file_name)
            except Exception as e:
                error_message=f'An error occured when trying to process files in save album media function: {str(e)}'
                logging.error(error_message)
                write_error(error_message)
                pass #! Remove pass when testing period is done
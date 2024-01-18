#todo create a class that may have to user albums as an inheritence 
# this class will have all functions related to downloading videos from an album

import os
from tools.service import prompt_permission
import requests #type: ignore
import pandas as pd
from db.data_functions import Data as Db
from config import Settings as Config
from .albums import AlbumRouter as Albums #type: ignore
import logging


class Downloads(Albums): #check that everything that imports classes has the import statement with 'Downloads' capitalizsed
    def __init__(self):
        self.Config = Config()
        self.savepath = self.Config.get_setting('videoSavepath')
        self.service = prompt_permission() #may not be needed since it inherits from album router
        self.album_id=self.search_album() #!subject to removal
    
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
        Data=Db() #? not sure if i have to make this a self argument ot not
        media_files = self.service.mediaItems().search(body={'albumId': album_id}).execute()['mediaItems']
        SavedMediaIds = Data.list_all_ids()
        album_media_ids = [item['id'] for item in media_files]
        
        for iteration, media_file in enumerate(media_files):
            file_name=media_file['filename'] #* changes in v2: uses the medias id to check if the video has been downloaded before
            download_url = media_file['baseUrl'] + '=d'
            mediafile_id = album_media_ids[iteration] #could use iter but this is what i know 
            if mediafile_id in SavedMediaIds:
                continue
            
            try:
                self.process_file(download_url, self.savepath, file_name)
            except Exception as e:
                logging.error(f'An error occured when trying to process files in save album media function: {str(e)}')
                pass #! Remove pass when testing period is done
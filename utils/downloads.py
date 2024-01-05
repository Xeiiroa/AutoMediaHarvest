#todo create a class that may have to user albums as an inheritence 
# this class will have all functions related to downloading videos from an album

import os
from tools.service import prompt_permission
import requests 
import pandas as pd
from db.data_functions import data as Data
from .albums import AlbumRouter


class downloads(AlbumRouter):
    def __init__(self):
        self.savepath = Data.get_video_save_path()
        self.service = prompt_permission()
        self.album_id=self.search_album()
    
    def process_file(self, url:str, destination_folder:str, file_name:str):
        response = requests.get(url)
        if response.status_code == 200:
            print('Downloading file {0}'.format(file_name))
            with open(os.path.join(destination_folder, file_name), 'wb') as f:
                f.write(response.content)
                f.close()
    
    
    
    def save_media(self,):
        media_files = self.service.mediaItems().search(body={})
        
        for media_file in media_files:
            file_name=media_file['filename'] #* changes in v2: uses the medias id to check if the video has been downloaded before
            download_url = media_file['baseUrl'] + '=d'
            """
            conditional checking for if the file has already been downloaded,
            
            - iterate over csv or database for the specific files media id 
            - if found pass/continue
            else run process file
        
            """
            self.process_file(download_url, self.savepath, file_name)
    
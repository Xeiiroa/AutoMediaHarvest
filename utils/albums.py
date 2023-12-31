from db.data_functions import data as Data
from setup import app
from setup import prompt_permission
import pandas as pd

from fastapi import APIRouter,HTTPException
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from google.oauth2 import service_account #type: ignore
from google.auth.transport.requests import Request as AuthRequest #type: ignore


class AlbumRouter():
    def __init__(self):
        #self.album_router=APIRouter()
        self.Data = Data()
        self.service = prompt_permission()
        #may add create album to init dependeing on app layout
        self.df_albums = self.list_albums()
        self.albumName = self.Data.get_album_name() #! Potential sql error when getting album name
     
    def list_albums(self):
        response = self.service.albums().list(
            pageSize=50,
            excludeNonAppCreatedData=False
        ).execute()

        listAlbums = response.get("albums")
        nextPageToken = response.get('nextPageToken')

        while nextPageToken:
            response = self.service.albums.list(
                pageSize=50,
                excludeNonAppCreatedData=False,
                pageToken=nextPageToken
            )
            listAlbums.append(response.get("albums"))
            nextPageToken = response.get('nextPageToken')

        df_albums = pd.DataFrame(listAlbums)
        return df_albums
    
    
    
        
    
    

        
    
        
        
    
    
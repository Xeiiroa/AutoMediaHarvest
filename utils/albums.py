from db.data_functions import data as Data
from setup import app
from setup import prompt_permission
import pandas as pd
import requests #type: ignore


from fastapi import APIRouter,HTTPException
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from google.oauth2 import service_account #type: ignore
from google.auth.transport.requests import Request as AuthRequest #type: ignore

from tools.envutils import load_variable


class AlbumRouter():
    def __init__(self):
        #self.album_router=APIRouter()
        self.Data = Data()
        self.service = prompt_permission()
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
    
    #search for an album by a specific name
    def search_album(self):
        try:
            filteredalbum=self.df_albums[self.df_albums["title"]==f"{self.albumName}"]["id"][0] #returns album id
            
            #returns all album information if id is successful
            #if not pandas returns a key error which with the try loop returns None
            response = self.service.albums().get(albumId=filteredalbum).execute() 
            return response
        except KeyError:
            return None

    
    def create_album(self):
        verifyAlbum = self.search_album() #may not be needed
        if not verifyAlbum:
            request_body = {
            'album': {
                'title': f"{self.albumName}",
                'coverPhotoMediaItemId': 'media/Default photo.jpg'}
            }
            response_album = self.service.albums().create(body=request_body).execute()
            
            #* add enrichments to album 
            #? (what allows search album to read the album after its been created)
            
            request_body = {
                'newEnrichmentItem': {
                    'textEnrichment': {
                        'text': 'This is my faily album'
                    }
                },
                'albumPosition': {
                    'position': 'LAST_IN_ALBUM'
                }
            }
            
            response = self.service.albums().addEnrichment(
                albumId=response_album.get('id'),
                body=request_body
            ).execute()
            return response_album
        else:
            return False
        
      
    
    
        
        
    
        
    
    

        
    
        
        
    
    
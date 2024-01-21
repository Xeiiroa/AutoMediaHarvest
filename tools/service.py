from envutils import load_variable # type: ignore
from Google import Create_Service # type: ignore
import pandas
#* may need to rework this in the case i need to create a new pickle file

# function that requests access to users google photos account
def prompt_permission():
    API_NAME = 'photoslibrary'
    API_VERSION = 'v1'
    google_client_secret = load_variable('GOOGLE_CLIENT_SECRET_JSON')
    SCOPES = ['https://www.googleapis.com/auth/photoslibrary',
          'https://www.googleapis.com/auth/photoslibrary.sharing',
      ]
    
   
    service = Create_Service(google_client_secret, API_NAME, API_VERSION, SCOPES)
    return service
  
if __name__ == '__main__':
  prompt_permission()
  
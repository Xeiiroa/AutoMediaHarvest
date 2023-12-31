from tools.envutils import load_variable
from tools.Google import Create_Service # type: ignore
import pandas

def prompt_permission():
    API_NAME = "photoslibrary"
    API_VERSION = "v1"
    google_client_secret = load_variable("GOOGLE_CLIENT_SECRET_JSON")
    SCOPES = ["https://www.googleapis.com/auth/photoslibrary",
          "https://www.googleapis.com/auth/photoslibrary.sharing"
    ]
    
   
    service = Create_Service(google_client_secret, API_NAME, API_VERSION, SCOPES)
    return service
    
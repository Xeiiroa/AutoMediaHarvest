#! SUBJECT TO DELETION


from google.oauth2 import service_account #type: ignore
from google.auth.transport.requests import Request #type: ignore
from tools.envutils import load_variable

SCOPES = ['https://www.googleapis.com/auth/photoslibrary']

# Your service account key file (JSON) and the Photos Library API credentials file
SERVICE_ACCOUNT_FILE = 'path/to/your/service_account_key.json'
CREDENTIALS_FILE = load_variable('GOOGLE_CLIENT_SECRET_JSON')


# Load your service account credentials
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)
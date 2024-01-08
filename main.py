from db import create_database
from utils.albums import AlbumRouter as albums
from utils.downloads import downloads as Downloads
from config import Settings as Config
from setup import AutoMediaHarvest as Script

def main():
    create_database()
    Config()
    Script()
    
        
if __name__ == "__main__":
    main()
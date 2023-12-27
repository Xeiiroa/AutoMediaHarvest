from db import create_database
from setup.app import create_app
from setup.routes import include_routers
from setup import prompt_permission

list_of_routers= [
    "routers.album.AlbumRouter"
]

def main():
    create_database()
    app = create_app()
    include_routers(app, list_of_routers)
    prompt_permission()
    
    
    
if __name__ == "__main__":
    main()
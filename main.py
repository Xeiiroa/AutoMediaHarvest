import argparse
import sys
import inspect
from db import create_database
from config import Settings as Config
from setup import AutoMediaHarvest as Script
import logging


def main():
    create_database()
    parser = argparse.ArgumentParser(description='run script')
    parser.add_argument('--settings', help='allows you to change settings', type=str) #value = None when called
    args = parser.parse_args() 
    
    if args.Config:
        Config = Config()
        
        try:
            if hasattr(Config, args.Config):
                getattr(Config, args.Config)()
            else:
                raise ValueError("Command does not exist")
        except Exception as e:
            logging.error(f'Command does not exist: {str(e)}')
        sys.exit()
    else:
        Script()
        
    
if __name__ == "__main__":
    main()

        

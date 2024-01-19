import argparse
import sys
import inspect
from db import create_database
from config import Settings as Config
from setup.schedule import AutoMediaHarvest as Script
import logging
import datetime
import os
from tools.error_report import write_error



def main():
    create_database()
    parser = argparse.ArgumentParser(description='run script')
    parser.add_argument('--Config', help='allows you to change settings', type=str) #value = None when called
    args = parser.parse_args() 
    
    if args.Config:
        Config = Config()
        
        try:
            if hasattr(Config, args.Config):
                getattr(Config, args.Config)()
            else:
                raise ValueError('Command does not exist')
        except Exception as e:
            error_message=f'Command does not exist: {str(e)}'
            logging.error(error_message)
        sys.exit()
    else:
        #cwd = os.getcwd()
        log_file = f'{os.getcwd()}/logs/runtime_logs.txt'
        timestamp(log_file)
        Script()


def timestamp(filelocation:str):
    with open(filelocation, 'a') as file:
        file.write(f'{datetime.datetime.now()} - the script ran \n')
        
    
    
if __name__ == '__main__':
    main()

        

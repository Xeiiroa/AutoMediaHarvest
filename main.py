import argparse
import sys
import inspect
from db import create_database
from config import Settings as Config
from setup.win_scheduler import AutoMediaHarvest as Script
import logging
import datetime
import os
from tools.error_report import write_error
from tools.runtime_log import runtime_log

create_database()
log_file = f'{os.getcwd()}/logs/runtime_logs.txt'

def main():
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
        runtime_log(log_file)
        Script()


        
def windows_scheduler():
    Script()
    runtime_log(log_file)
    
    
    
if __name__ == '__main__': #check for if the program runs without actually calling main and if so delete windows shceduler function
    main()   
"""else:
    windows_scheduler()"""
    

        

import os
import datetime
from .envutils import load_variable


cwd = os.getcwd()
logs_folder = os.path.join(cwd, 'logs', 'errors.txt')
def write_error(error, logsFolderLocation=logs_folder):
    with open(logsFolderLocation, 'a') as file:
        file.write(f'{datetime.datetime.now()} - {error}')
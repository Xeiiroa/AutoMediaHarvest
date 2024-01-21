import datetime


def runtime_log(filelocation:str):
    with open(filelocation, 'a') as file:
        file.write(f'{datetime.datetime.now()} - the script ran \n')
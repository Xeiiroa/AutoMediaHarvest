import configparser
import os
from tkinter import filedialog

class Settings:
    def __init__(self):
        
        cwd = os.getcwd()
        self.settingsFilepath = cwd + '/config'
        self.settingsFilename = 'settings.ini'
        self.config = configparser.ConfigParser()
        
        self.defaultSettings = {
            'Savepaths':{
                'videoSavepath': f'{default_video_path}/media'
            },
            'AlbumName':{
                'albumName': 'AutoMediaHarvest'
            }   
        }
        
        
        self.create_settings_file(self.settingsFilename, self.default_settings, self.settingsFilepath)
    

    def create_settings_file(self, filepath, sections, destination_directory):
        try:
            fullFilepath = os.path.join(destination_directory, filepath)
            
            if os.path.exists(fullFilepath): #put in full filepath into parentheses
                raise FileExistsError
            
            for section_name, section_values in sections.items():
                config.add_section(section_name)
                for key, value in section_values.items():
                    config.set(section_name, key, str(value))             
            
            with open(fullFilepath, w) as config_file:
                config.write(config_file)
        
        except FileExistsError:
            pass
    
    def list_settings(self):
        ...
        #todo iterate over the sections of the ini file and list all the keys under each section
        #not sure if i also want to print the current value but its something i can do
        """
        ex:
        Settings from {settings.ini}: can add filename as a param for future versitility
        
        Savepaths:
            videoSavepath
            
        Albumname:
            albumName
        
        """
    
    
    
    def change_video_savepath(self):
        self.config.read(self.settingsFilename)
        
        new_savepath = filedialog.askdirectory(title='Select a folder')
        
        config.set('Savepaths', 'VideoSavepath', new_savepath)
        
        with open(self.settingFilename, 'w') as config_file:
            config.write(config_file)
    
    def get_setting(self, settingName:str):
        ...
        #todo function that gets the value of a specific named variable
        
        """
        expected return
        
        Error catching
        Variable not found: return error message
        """
    
            



config = configparser.ConfigParser()
config.read('settings.ini')

default_video_path = os.getcwd()



def default_config(): #creates the programs default settings on its first run
    defaultSettings = {
    'videoSavepath': f'{default_video_path}/media',
    'albumName': 'AutoMediaHarvest'
    }
    
    for setting in defaultSettings:
        ...
    
    

    
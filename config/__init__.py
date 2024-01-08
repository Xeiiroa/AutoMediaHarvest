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
                'videoSavepath': f'{cwd}/media'
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
                self.config.add_section(section_name)
                for key, value in section_values.items():
                    self.config.set(section_name, key, str(value))             
            
            with open(fullFilepath, 'w') as config_file:
                self.config.write(config_file)
        
        except FileExistsError:
            pass
    
    def list_settings(self):                                       
        self.config.read(self.settingsFilename)
        
        allKeys = {}
        
        for section in self.config.sections():
            keys = self.config.options(section)
            
            allKeys[section] = keys
            
        return allKeys
    
    
    
    def change_video_savepath(self):
        self.config.read(self.settingsFilename)
        
        new_savepath = filedialog.askdirectory(title='Select a folder')
        
        self.config.set('Savepaths', 'VideoSavepath', new_savepath)
        
        with open(self.settingFilename, 'w') as config_file:
            self.config.write(config_file)
    
    def get_setting(self, settingName:str):
        #todo function that gets the value of a specific named variable
        try:
        
            self.config.read(self.settingsFilename)
            
            for section in self.config.sections():
                if self.config.has_option(section, settingName):
                    result = self.config.get(section, settingName)
                    return result
            raise Exception
        except Exception:
            pass
        
    def change_setting(self, settingName, newSettingValue):
        self.config.read(self.settingsFilename)
        
        for section in self.config.sections():
            if self.config.has_option(section, settingName):
                
                self.config.set(section, settingName, newSettingValue)
                
                with open(self.settingsFilename, 'w') as config_file:
                    self.config.write(config_file)
        
        

    
            






    

    
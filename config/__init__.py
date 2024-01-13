import configparser
from configparser import SafeConfigParser
import os
from tkinter import filedialog

class Settings:
    def __init__(self):
        
        cwd = os.getcwd()
        self.settingsFilepath = cwd + '/config'
        self.settingsFilename = 'settings.ini'
        self.fullSettingsFilepath = f'{cwd}/config/{self.settingsFilename}'
        self.config = configparser.ConfigParser()
        
        self.defaultSettings = {
            'Downloads':{
                'videoSavepath': f'{cwd}/media'
            },
            'Albums':{
                'albumName': 'AutoMediaHarvest'
            }   
        }
        
        
        self.create_settings_file(self.settingsFilename, self.defaultSettings, self.settingsFilepath)
    

    def create_settings_file(self, filepath, sections: dict, destination_directory):
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
        if os.path.isfile(self.fullSettingsFilepath):                                       
            self.config.read(self.fullSettingsFilepath)
            
            
            allKeys = {}
            
            for section in self.config.sections():
                keys = self.config.options(section)
                
                allKeys[section] = keys
                
            return allKeys
        else:
            return 404
   
    
    
    def change_video_savepath(self): #ended off here
        self.config.read(self.fullSettingsFilepath)
    
        new_savepath = filedialog.askdirectory(title='Select a folder')
        
        self.config.set('Downloads', 'videosavepath', new_savepath)
        
        with open(self.fullSettingsFilepath, 'w') as config_file:
            self.config.write(config_file)
            
        return 200
        
        
        
        
    
    def get_setting(self, settingName:str):
        #todo function that gets the value of a specific named variable iterating over all sections to do so (causes problems when it comes to a larger project)
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
        #todo: add exception handling for if a setting doesnt match the name of any settings in the ini file
        self.config.read(self.settingsFilename)
        
        for section in self.config.sections():
            if self.config.has_option(section, settingName):
                
                self.config.set(section, settingName, newSettingValue)
                
                with open(self.settingsFilename, 'w') as config_file:
                    self.config.write(config_file)
        
        

    
            






    

    
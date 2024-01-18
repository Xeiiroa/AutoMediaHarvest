import configparser
import os
from tkinter import filedialog
import logging

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
        
        
    def help(self):
        functions_list = [name for name in dir(self) if callable(getattr(self, name)) and not name.startswith('__')]
        functions = '\nList of commands: \n-------\n'
        for function in functions_list:
            if function == 'help':
                continue
            functions += f'{function}\n'
        print(functions)
        return functions
        
    def create_settings_file(self, filepath, sections: dict, destination_directory):
        try:
            fullFilepath = os.path.join(destination_directory, filepath)
            
            if os.path.exists(fullFilepath):
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
   
    
    
    def change_video_savepath(self): 
        self.config.read(self.fullSettingsFilepath)
    
        new_savepath = filedialog.askdirectory(title='Select a folder')
        
        self.config.set('Downloads', 'videosavepath', new_savepath)
        
        with open(self.fullSettingsFilepath, 'w') as config_file:
            self.config.write(config_file)
            
        return 200
        
    def get_setting(self, settingName:str): #*case insensitive
        #todo function that gets the value of a specific named variable iterating over all sections to do so (causes problems when it comes to a larger project)
        
        """
        ___Changes___
        same as change setting
        """
        try:
        
            self.config.read(self.fullSettingsFilepath)
            
            for section in self.config.sections():
                if self.config.has_option(section, settingName):
                    result = self.config.get(section, settingName)
                    return result
            raise Exception
        except Exception:
            pass
        
    def change_setting(self, settingName:str, newSettingValue):
        #todo: add exception handling for if a setting doesnt match the name of any settings in the ini file
        """
        Possible changes
        ___newSettingValue___
        - Make it so that new setting value takes user input insteed of being a flat parameter to avoid problems with mistypes
        - add a text to function to make sure that the user wants to change this settting to this value (f'Are you sure you want to change {settingName} to {newSettingValue}? Y/N'(make it case insnsitive ofc))
        
        ___Requirements___
        - Early in the function verify that the .ini file has the setting and if not reprompt the user to define the setting name
            - with this being the case id have to also set the setting name to be a user input
        """
        #can also make it so that it takes input for the new setting in case of mistypes, this way it voids all error checking or i can set a confirmation (are you sure y/n)
        self.config.read(self.fullSettingsFilepath)

        try:
        
            for section in self.config.sections():
                if self.config.has_option(section, settingName):
                    
                    self.config.set(section, settingName, newSettingValue)
                    
                    with open(self.fullSettingsFilepath, 'w') as config_file:
                        self.config.write(config_file)
        except Exception as e:
            logging.error(f'An error has occured when trying to change a setting')
            
        
        

    
            






    

    
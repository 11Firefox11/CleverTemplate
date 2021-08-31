import os
configfile = 'ct-config.json'

class ConfigFileNotInPath(Exception):
    def __init__(self, path, message=f"path must contain ct config file ({configfile})"):
        self.path = os.path.abspath(path)
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return f"path: '{self.path}' -> {self.message}"

class PathDoesNotExist(Exception):
    def __init__(self, path, message=f"path does not exists"):
        self.path = os.path.abspath(path)
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return f"path: '{self.path}' -> {self.message}"

class PathAlreadyExist(Exception):
    def __init__(self, path, message=f"path already exists"):
        self.path = os.path.abspath(path)
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return f"path: '{self.path}' -> {self.message}"

class ConfigFileSyntax(Exception):
    def __init__(self, path, message=f"config file can't find any files to use in the directory, bad syntax"):
        self.path = os.path.abspath(path)
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return f"path: '{self.path}' -> {self.message}"

class ParameterOptions(Exception):
    def __init__(self, parameteroptions, message=f"parameter option error"):
        self.parameteroptions = parameteroptions
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return f"parameteroptions: '{self.parameteroptions}' -> {self.message}"
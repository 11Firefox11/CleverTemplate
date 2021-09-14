class DefaultCleverTemplateException(Exception):
    def __init__(self, object, objecttype="object", message=f"object error", errorname="CleverTemplateError"):
        self.objecttype = objecttype
        self.object = object
        self.message = message
        self.errorname = errorname
        super().__init__(self.message)
    
    def __str__(self):
        return f"{self.errorname}: {self.objecttype}: '{self.object}' -> {self.message}."

class PathMustBe(DefaultCleverTemplateException):
    def __init__(self, path, objecttype="path", message="path must point to an existing ", mustbetype="directory"):
        super().__init__(path, objecttype=objecttype, message=message+mustbetype, errorname=self.__class__.__name__)

class ParameterOptions(DefaultCleverTemplateException):
    def __init__(self, options, objecttype="parameter option", message=""):
        super().__init__(options, objecttype=objecttype, message=message, errorname=self.__class__.__name__)

class ConfigFileSyntaxError(DefaultCleverTemplateException):
    def __init__(self, path, objecttype="config file", message="syntax error"):
        super().__init__(path, objecttype=objecttype, message=message, errorname=self.__class__.__name__)

class CustomParameterValue(DefaultCleverTemplateException):
    def __init__(self, value, realparamoption, objecttype="parameter option", message=""):
        super().__init__(value, objecttype=objecttype, message=message+realparamoption, errorname=self.__class__.__name__)
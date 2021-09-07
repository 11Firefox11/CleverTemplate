class DefaultCleverTemplateException(Exception):
    def __init__(self, object, objecttype="object", message=f"object error"):
        self.objecttype = objecttype
        self.object = object
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return f"{self.objecttype}: '{self.object}' -> {self.message}"

class PathMustBe(DefaultCleverTemplateException):
    def __init__(self, path, objecttype="path", message="path must point to an existing ", mustbetype="directory"):
        super().__init__(path, objecttype=objecttype, message=message+mustbetype)
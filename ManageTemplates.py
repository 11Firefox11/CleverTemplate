import os, pathlib, CleverTemplateErrors
from jinja2 import Template

def CreateTemplate(path, data):
    if os.path.isfile(path):
        template = Template(str(open(path, "r").read()))
        return template.render(data=data)
    else:
        raise CleverTemplateErrors.ConfigFileNotInPath(path)

def SaveTemplate(path, data, customfile=None, forcecustom=True):
    if os.path.isfile(path):
        dir = os.path.abspath(str(pathlib.Path(path).parent))
        customfile = os.path.split(path)[1]
    elif customfile == None:
        return False 
    else:
        dir = path
        os.mkdir(dir)
    file = customfile
    if customfile == None or forcecustom == True:
        if customfile == None:
            customfile = str(os.path.abspath(path)).split(os.sep)[-1]
        if os.path.exists(os.path.join(dir, customfile)):
            n = 0
            while True:
                n += 1
                file = "{0}_{2}.{1}".format(*customfile.rsplit('.', 1) + [n])
                fullfilepath = os.path.join(dir, file)
                if os.path.exists(fullfilepath) == False:
                    break
    fullfilepath = os.path.join(dir, file)
    if os.path.exists(fullfilepath) == False:
        open(fullfilepath, "w+").write(data)
        return fullfilepath
    else:
        raise CleverTemplateErrors.PathAlreadyExist(path)
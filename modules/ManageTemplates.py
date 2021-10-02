import os
from jinja2 import Template
from .CtExceptions import *

class CleverTemplate:

    NameExtendPhrase = "ct"
    OutputFolder = "ct-output"

    def __init__(self, path):
        self.path = path

    def CreateTemplate(self, data, customname=None, forcename=False, customdir=None, forcedir=True, addphrase=False):
        if customname == None:
            customname = self.file
        if customdir == None:
            customdir = os.path.join(self.directory, CleverTemplate.OutputFolder)
        savepath = CleverTemplate.generate_save_path(customdir, customname, forcename, forcedir, addphrase)
        open(savepath, "w+").write(CleverTemplate.render_template(self.path, data))
        return savepath

    @property
    def path(self):
        return os.path.join(self.directory, self.file)

    @path.setter
    def path(self, fullpath):
        if CleverTemplate.file_exists(fullpath):
            self.directory, self.file = os.path.split(fullpath)

    @staticmethod
    def generate_save_path(outputpath, file, forcename=False, forcedir=True, addphrase=False):
        outputstatus = CleverTemplate.dir_exists(outputpath, forcedir)
        if outputstatus:
            if forcename == False:
                n = ""
                while True:
                    custfile = "{0}{2}.{1}".format(*file.rsplit('.', 1) + [n])
                    if addphrase:
                        fullpath = os.path.join(outputpath, CleverTemplate.NameExtendPhrase + "-" + custfile)
                    else:
                        fullpath = os.path.join(outputpath, custfile)
                    try:
                        CleverTemplate.file_exists(fullpath)
                    except PathMustBe:
                        break
                    if n == "":
                        n = 1
                    else:
                        n += 1
            else:
                fullpath = os.path.join(outputpath, file)
            return fullpath

    @staticmethod
    def render_template(path, data):
        if CleverTemplate.file_exists(path):
            template = Template(str(open(path, "r").read()))
            return template.render(ctdata=data)

    @staticmethod
    def dir_exists(directory, forcedir=False):
        if forcedir:
            try:
                os.mkdir(directory)
            except:
                pass
        if os.path.isdir(directory):
            return True
        else:
            raise PathMustBe(directory, mustbetype="directory")

    @staticmethod
    def file_exists(filepath):
        if os.path.isfile(filepath):
            return True
        else:
            raise PathMustBe(filepath, mustbetype="file")

    @classmethod
    def set_NameExtendPhrase(cls, value):
        cls.NameExtendPhrase = value

    @classmethod
    def set_OutputFolder(cls, value):
        cls.OutputFolder = value
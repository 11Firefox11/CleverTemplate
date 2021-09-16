from CtExceptions import *
import os, json, pathlib

class CleverConfig:

    ConfigFile = "ct-config.json"
    parameterobj = {
    "text": {"type": str, "defval": "None"},
    "number": {"type": float, "defval": 1},
    "boolean": {"type": bool, "defval": True},
    }

    def __init__(self, path):
        self.configpath = path
        self.skippedfiles = []
        self.skippedparameters = {}

    def ConfigParameters(self, forcedefparval=True, checkparams=None):
        data = self.validfilesdict
        output = {}
        for file in data:
            if checkparams == None or file in checkparams and type(checkparams) == dict:
                params = {}
                skips = {}
                for param in data[file]:
                    if checkparams == None:
                        if param != None and param not in params:
                            paramoptions = data[file][param]
                            try:
                                params[param] = CleverConfig.check_parameteroptions(paramoptions, forcedefparval)
                            except Exception as e:
                                skips[param] = str(e)
                    else:
                        if file in checkparams and param in checkparams[file]:
                            currentparam = data[file][param]
                            currentcustomparam = checkparams[file][param]
                            try:
                                if CleverConfig.parameterobj[currentparam[0]]['type'] == type(currentcustomparam) and currentcustomparam != "":
                                    params[param] = currentcustomparam
                                elif len(currentparam) > 1 and CleverConfig.parameterobj[currentparam[0]]['type'] == type(currentparam[1]):
                                    params[param] = currentparam[1]
                                elif forcedefparval:
                                    params[param] = CleverConfig.parameterobj[currentparam[1]]['defval']
                                else:
                                    raise CustomParameterValue(currentcustomparam, currentparam[0], "custom parameter value", "does not match with the actual config file parameter type: ")
                            except Exception as e:
                                skips[param] = str(e)
                if params != {}:
                    output[file] = params
                if skips != {}:
                    self.skippedparameters[file] = skips
        return output

    @staticmethod
    def check_parameteroptions(options, forcedefval=True):
        if len(options) > 0 and type(options) == list:
            if options[0] in CleverConfig.parameterobj:
                paramtype = CleverConfig.parameterobj[options[0]]['type']
                if len(options) > 1 and type(options[1]) != paramtype or len(options) == 1:
                    if forcedefval:
                        currdefval = CleverConfig.parameterobj[options[0]]['defval']
                        if len(options) > 1:
                            options[1] = currdefval
                        else:
                            options.append(currdefval)
                    else:
                        raise ParameterOptions(options, message=f"parameter does not have default value")
            else:
                raise ParameterOptions(options, message=f"'{options[0]}' is not a valid parameter type")
        else:
            raise ParameterOptions(options, message="parameter options can't be empty")
        return options

    @property
    def validfilesdict(self):
        data = self.configcontent
        outputdata = {}
        maindir = pathlib.Path(self.configpath).parent
        for file in data:
            fullfile = os.path.join(maindir, file)
            if os.path.isfile(fullfile):
                outputdata[fullfile] = data[file]
            else:
                self.skippedfiles.append(fullfile)
        if outputdata != {}:
            return outputdata
        else:
            raise ConfigFileSyntaxError(self.ConfigFile, message="can't find any existing files to use in the directory, bad syntax")

    @property
    def configcontent(self):
        return json.load(open(self.configpath))

    @property
    def configpath(self):
        canbepaths = [self.path, os.path.join(self.path, CleverConfig.ConfigFile)]
        for canbepath in canbepaths:
            if os.path.isfile(canbepath):
                return os.path.abspath(canbepath)
        raise PathMustBe(self.path, "path", mustbetype=f"directory that contains the {CleverConfig.ConfigFile} file, or must point directly on the file")

    @configpath.setter
    def configpath(self, path):
        self.path = path

    @classmethod
    def set_configfile(cls, filename):
        cls.ConfigFile = filename
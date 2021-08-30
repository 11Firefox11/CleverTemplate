import os, json, pathlib, CleverTemplateErrors

configfile = "ct-config.json"

parameterobj = {
    "text": {"type": str, "defval": "None"},
    "number": {"type": float, "defval": 1},
    "boolean": {"type": bool, "defval": True},
}

def CheckPath(path):
    canbepaths = [path, os.path.join(path, configfile)]
    for canpath in canbepaths:
        if os.path.isfile(canpath):
            return canpath
    raise CleverTemplateErrors.ConfigFileNotInPath(path)

def ReadConfigJson(path):
    configpath = CheckPath(path)
    if configpath:
        return json.load(open(configpath,))

def CheckFiles(path):
    data = ReadConfigJson(path)
    if data:
        enddata = {}
        if os.path.isfile(path):
            maindir = pathlib.Path(path).parent
        elif os.path.isdir(path):
            maindir = path
        for file in data:
            if os.path.isfile(os.path.join(maindir, file)):
                enddata[file] = data[file]
        return enddata

def CheckParameterOptions(options, forcedefval=True):
    output = {}
    if len(options) > 0 and type(options) == list:
        if options[0] in parameterobj:
            paramtype = parameterobj[options[0]]["type"]
            if len(options) > 1 and type(options[1]) != paramtype or len(options) == 1:
                if forcedefval:
                    currdefval =  parameterobj[options[0]]['defval']
                    if len(options) > 1:
                        options[1] = currdefval
                    else:
                        options.append(currdefval)
                else:
                    raise CleverTemplateErrors.ParameterOptions(options, "parameter does not have default value")
            output = options
        else:
            raise CleverTemplateErrors.ParameterOptions(options, f"{options[0]} is not a parameter type")
    else:
        raise CleverTemplateErrors.ParameterOptions(options, "parameter options can't be empty")
    return output

def GroupParameters(path, forcedefparval=True, canprint=True):
    data = CheckFiles(path)
    output = {}
    skips = {}
    if data != False:
        for file in data:
            params = {}
            skip = {}
            for param in data[file]:
                if param != None and param not in params:
                    paramoptions = data[file][param]
                    try:
                        paramcheck = CheckParameterOptions(paramoptions, forcedefparval)
                        if paramcheck:
                            params[param] = paramcheck
                    except Exception as e:
                        if canprint:
                            skip[param] = e
            if params != {}:
                output[file] = params
            if skip != {}:
                skips[file] = skip
        if output == {}:
            pathinerror = CheckPath(path)
            raise CleverTemplateErrors.ConfigFileSyntax(pathinerror)
        return output, skips

def CheckCustomParameters(path, customparams, forcedefval=True):
    data = GroupParameters(path, forcedefval)[0]
    output = {}
    if data != False:
        for file in data:
            if file in customparams:
                params = {}
                for param in data[file]:
                    if param in customparams[file]:
                        currentparam = data[file][param]
                        currentcustomparam = customparams[file][param]
                        if parameterobj[currentparam[0]]['type'] == type(currentcustomparam):
                            params[param] = currentcustomparam
                        elif len(currentparam) > 1:
                            params[param] = currentparam[1]
                        elif forcedefval:
                            params[param] = parameterobj[currentparam[1]]['defval']
                if params != {}:
                    output[file] = params
        return output
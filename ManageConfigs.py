import os, json, pathlib

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
    return False

def ReadConfigJson(path):
    configpath = CheckPath(path)
    if configpath:
        return json.load(open(configpath,))
    else:
        return False

def CheckFiles(path):
    data = ReadConfigJson(path)
    enddata = {}
    if data:
        if os.path.isfile(path):
            maindir = pathlib.Path(path).parent
        elif os.path.isdir(path):
            maindir = path
        for file in data:
            if os.path.isfile(os.path.join(maindir, file)):
                enddata[file] = data[file]
        return enddata
    else:
        return False

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
                    return False
            output = options
        else:
            return False
    else:
        return False
    return output

def GroupParameters(path, forcedefparval=True):
    data = CheckFiles(path)
    output = {}
    if data != False:
        for file in data:
            params = {}
            for param in data[file]:
                if param != None:
                    paramoptions = data[file][param]
                    paramcheck = CheckParameterOptions(paramoptions, forcedefparval)
                    if paramcheck:
                        params[param] = paramcheck
            if params != {}:
                output[file] = params
        return output
    else:
        return False

def CheckCustomParameters(path, customparams, forcedefval=True):
    data = GroupParameters(path, forcedefval)
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
    else:
        return False
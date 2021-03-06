import os, argparse, pathlib, sys, json, copy
from modules.ManageConfigs import CleverConfig
from modules.ManageTemplates import CleverTemplate
from modules.CtExceptions import *

class Main:

    Version = "1.2.0"
    OutputTypes = {"info":"INFO", "input":"INPUT", "error": "ERROR"}
    DefHelpInfoText = "For help in this curtain topic, visit:"
    DefEpilog = "For more information and help, go to the app's github page: https://github.com/11Firefox11/CleverTemplate."
    DefInputCommands = {"!ml":"multipleline == False and listinput == False", "!qml":"multipleline == True", "!qlist":"listinput == True"}

    def __init__(self):
        self.Commands = {
        "create":{"args": {"path":{"help":"Specify path to the ct-config.json."}, "--customdata":{"help":"Specify a path to a custom data as input (json file)."}},"desc":"Create a template, by giving the path of the ct-config.json.", "help":"Create template.", "func":Main.create, "version":"1.1.0"}}
        self.InitArgparse()

    def InitArgparse(self):
        parser = argparse.ArgumentParser(add_help=False, description=f"Clever Template - {Main.Version}", epilog=Main.DefEpilog) 
        subparsers = parser.add_subparsers(help='List of available commands.')
        for command in self.Commands:
            commanddict = self.Commands[command]
            commandparse = subparsers.add_parser(command, help=commanddict["help"], add_help=False, description=commanddict["desc"])
            for arg in commanddict["args"]:
                argdict = commanddict["args"][arg]
                if "default" not in argdict:
                    argdict["default"] = None
                commandparse.add_argument(arg, help=argdict["help"], default=argdict["default"])
            commandparse.add_argument('--help', '-h', action='help', default=argparse.SUPPRESS, help=f"Show help about this command ({command}).")
            commandparse.add_argument('--version','-v', action='version',version=f"{Main.OutputTypes['info']}: Command '{command}' version: {self.Commands[command]['version']}", help="Shows commands's version number.")
            commandparse.set_defaults(func=commanddict['func'])
        parser.add_argument('--version','-v', action='version',version=f"Clever Template version: {Main.Version}", help="Shows app's version number.")
        parser.add_argument('--help','-h', action='help', default=argparse.SUPPRESS, help='Shows help about the app.')
        args = parser.parse_args()
        try:
            args.func(self, args)
        except Exception as e:
            exc_type = str(sys.exc_info()[0])
            if e.__class__.__name__ == "AttributeError":
                parser.print_help()
            else:
                self.Output("info", "Ouh...an error occurred...")
                if "json" in exc_type:
                    self.Output("error", ConfigFileSyntaxError(self.config.configpath, message=f"Bad JSON syntax. {Main.DefHelpInfoText} https://www.json.org/"))
                elif "jinja2" in exc_type:
                    self.Output("error", DefaultCleverTemplateException(self.currfile, "template file",f"Bad Jinja2 syntax. Check your variables, and the default syntaxes. {Main.DefHelpInfoText} https://jinja.palletsprojects.com/en/3.0.x/templates/"))
                else:
                    self.Output("error", e)
                self.Output("info", Main.DefEpilog)

    def create(self, args):
        self.config = CleverConfig(args.path)
        self.Output("info", f"Scanning config file at path: '{os.path.abspath(self.config.configpath)}'...")
        self.skippedall = False
        data = self.config.ConfigParameters()
        skips = [self.config.skippedfiles, self.config.skippedparameters]
        for skipindex in range(len(skips)):
            skip = skips[skipindex]
            if len(skip) > 0:
                for file in skip:
                    fullpath = os.path.abspath(file)
                    if skipindex == 0:
                        self.Output("info", f"Skipped file: '{fullpath}', file does not exists.")
                    else:
                        for param in skip[file]:
                            self.Output("info", f"Skipped parameter: '{param}' at '{file}', {skip[file][param]}.")
        self.Output("info", "Scanning done.")
        customdata = {}
        if data:
            if args.customdata == None:
                for file in data:
                    self.currfile = file
                    self.Output("info", f"Editing '{file}' parameters: ")
                    params = {}
                    for param in data[file]:
                        paramtype = data[file][param][0]
                        listinput = False
                        multipleline = False
                        if data[file][param][0] == "list":
                            self.Output("info", "Type: `!qlist` for quiting list input.")
                            listinput = True
                        else:
                            self.Output("info", "Type: `!ml` for multi line input, and type `!qml` for exiting multi line input mode!")
                        self.Output("info", f"Parameter: '{param}', type: '{paramtype}', default value: '{data[file][param][1]}'")
                        if listinput:
                            inputdata = []
                            plusprint = " <LIST>"
                        else:
                            inputdata = ""
                            plusprint = ""
                        while True:
                            self.Output("input", "", endprint="", aftertype=plusprint)
                            try:
                                currinput =  input()
                            except:
                                exit()
                            for command in Main.DefInputCommands:
                                if currinput == command and eval(Main.DefInputCommands[command]):
                                    if "ml" in command:
                                        multipleline = not eval(Main.DefInputCommands[command].split(" ")[-1])
                                    else:
                                        listinput = False
                                    currinput = ""
                            if multipleline == True:
                                plusprint = " <MULTI LINE>"
                            if multipleline == False and listinput == False:
                                if currinput != "":
                                    if len(inputdata) > 0 and inputdata[-1] == "\n":
                                        inputdata = inputdata[:-1]
                                    else:
                                        if type(inputdata) != list:
                                            inputdata += currinput
                                        else:
                                            inputdata.append(currinput)
                                params[param] = inputdata
                                break
                            else:
                                if currinput != "":
                                    if multipleline == True:
                                        inputdata += currinput + "\n"
                                    elif listinput == True:
                                        inputdata.append(currinput)
                    customdata[file] = params
                    self.Output("info", f"Finished with '{file}'.")
            else:
                if os.path.isfile(args.customdata):
                    customdata = json.load(open(args.customdata))
                    data = {}
                    for file in customdata:
                        fullcurrpath = os.path.join(pathlib.Path(self.config.path).parent, file)
                        if CleverTemplate.file_exists(fullcurrpath):
                            data[fullcurrpath] = copy.deepcopy(customdata[file])
                    customdata = copy.deepcopy(data)
                else:
                    raise PathMustBe(args.customdata, mustbetype="custom data file")
            customdata = self.config.ConfigParameters(checkparams=customdata)
            for file in customdata:
                self.currfile = file
                self.Output("info", f"Creating template '{file}'.")
                templatefile = os.path.join(pathlib.Path(self.config.configpath).parent, file)
                template = CleverTemplate(templatefile)
                outputpath = os.path.abspath(template.CreateTemplate(customdata[file]))
                self.Output("info", f"Template created at '{outputpath}', with parameters: '{customdata[file]}'.")
        else:
            self.Output("error", ConfigFileSyntaxError(self.config.configpath, message=f"Nothing to do, all parameters or/and files skipped."))

    @staticmethod
    def Output(outputtype, text, endprint="\n", aftertype=""):
        text = f"{Main.OutputTypes[outputtype]}{aftertype}: {str(text)}"
        if outputtype in Main.OutputTypes:
            print(str(text), end=endprint)

if __name__ == "__main__":
    Main()
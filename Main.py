import os, argparse, pathlib, traceback
from modules.ManageConfigs import CleverConfig
from modules.ManageTemplates import CleverTemplate

class Main:

    Mainpath = os.path.dirname(os.path.realpath(__file__))
    Version = "1.0"
    OutputTypes = {"info":"INFO: ", "input":"INPUT: "}

    def __init__(self):
        self.lastprintlen = 0
        self.Commands = {
        "create":{"args": {"path":{"help":"Specify path to the ct-config.json."}},"desc":"Create a template, by giving the path of the ct-config.json.", "help":"Create template.", "func":Main.create, "version":"1.0"}}
        self.InitArgparse()

    def InitArgparse(self):
        parser = argparse.ArgumentParser(add_help=False, description=f"Clever Template - {Main.Version}", epilog="For more information, help, go to the app's github page: https://github.com/11Firefox11/CleverTemplate.") 
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
            commandparse.add_argument('--version','-v', action='version',version=f"Command '{command}' version: {self.Commands[command]['version']}", help="Shows commands's version number.")
            commandparse.set_defaults(func=commanddict['func'])
        parser.add_argument('--version','-v', action='version',version=f"Clever Template version: {Main.Version}", help="Shows app's version number.")
        parser.add_argument('--help','-h', action='help', default=argparse.SUPPRESS, help='Shows help about the app.')
        args = parser.parse_args()
        try:
            args.func(self, args)
        except Exception as e:
            if e.__class__.__name__ == "AttributeError":
                parser.print_help()
            else:
                print("Ouh...an error occurred...")
                traceback.print_exc()
                print(e)

    def create(self, args):
        config = CleverConfig(args.path)
        self.Output("info", f"Scanning config file at path: '{os.path.abspath(config.configpath)}'...")
        data = config.ConfigParameters()
        skips = [config.skippedfiles, config.skippedparameters]
        for skipindex in range(len(skips)):
            skip = skips[skipindex]
            if len(skip) > 0:
                for file in skip:
                    fullpath = {os.path.abspath(file)}
                    if skipindex == 0:
                        self.Output("info", f"Skipped file: '{fullpath}', file does not exists.")
                    else:
                        for param in skip[file]:
                            self.Output("info", f"Skipped parameter: '{param}' at '{file}', {skip[file][param]}.")
        self.Output("info", "Scanning done.")
        customdata = {}
        for file in data:
            self.Output("info", f"Editing '{file}' parameters: ")
            params = {}
            for param in data[file]:
                self.Output("input", f"Parameter: '{param}', type: '{data[file][param][0]}', default value: '{data[file][param][1]}:': ", "")
                params[param] =  input()
            customdata[file] = params
            self.Output("info", f"Finished with '{file}'.")
        customdata = config.ConfigParameters(checkparams=customdata)
        for file in customdata:
            self.Output("info", f"Creating template '{file}'.")
            templatefile = os.path.join(pathlib.Path(config.configpath).parent, file)
            template = CleverTemplate(templatefile)
            outputpath = os.path.abspath(template.CreateTemplate(customdata[file]))
            self.Output("info", f"Template created at '{outputpath}', with parameters: '{customdata[file]}'.")

    @staticmethod
    def Output(outputtype, text, endprint="\n"):
        text = Main.OutputTypes[outputtype]+ text
        if outputtype in Main.OutputTypes:
            print(text, end=endprint)

if __name__ == "__main__":
    Main()